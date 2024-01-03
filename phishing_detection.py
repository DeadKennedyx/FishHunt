import re
import http.client
import base64
import joblib

# Load the model and vectorizer
model = joblib.load('phishing_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

def extract_urls_from_text(text):
    url_regex = r'https?://[^\s]+'
    return re.findall(url_regex, text)

def fetch_bad_domains():
    conn = http.client.HTTPSConnection("raw.githubusercontent.com")
    conn.request("GET", "/stamparm/aux/master/maltrail-malware-domains.txt")
    response = conn.getresponse()
    if response.status == 200:
        return set(response.read().decode().splitlines())
    else:
        print("Failed to fetch bad domains")
        return set()

def preprocess_email(email):
    # Add your email preprocessing logic here (if needed)
    return email.lower()

def check_phishing(service, user_id='me', max_results=100, threshold=0.97):
    response = service.users().messages().list(userId=user_id).execute()
    messages = response.get('messages', [])
    bad_domains = fetch_bad_domains()

    for message in messages[:max_results]:
        msg = service.users().messages().get(userId=user_id, id=message['id']).execute()
        payload = msg.get('payload', {})
        parts = payload.get('parts', [])
        for part in parts:
            body_data = part['body'].get('data', '')
            decoded_data = base64.urlsafe_b64decode(body_data.encode('ASCII')).decode('utf-8')
            urls = extract_urls_from_text(decoded_data)

            # Check email content
            processed_data = preprocess_email(decoded_data)
            email_vector = vectorizer.transform([processed_data])
            phishing_prediction = model.predict(email_vector)

            # Check URLs
            bad_domain_found = any(domain in bad_domains for url in urls for domain in url.split('/')[2:3])

            if model.predict_proba(email_vector)[0][1] > threshold or bad_domain_found:
                print(f"Phishing email detected: {msg['snippet']}")

