import mailbox
from bs4 import BeautifulSoup
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
import joblib


def extract_emails(mbox_file, label):
    emails = []
    mbox = mailbox.mbox(mbox_file)
    for message in mbox:
        subject = message['subject']
        sender = message['from']
        payload = ""

        if message.is_multipart():
            for part in message.get_payload():
                # Check if the payload is None
                if part.get_payload(decode=True) is not None:
                    payload += str(part.get_payload(decode=True), 'utf-8', 'ignore')
        else:
            # Check if the payload is None
            if message.get_payload(decode=True) is not None:
                payload = str(message.get_payload(decode=True), 'utf-8', 'ignore')
        
        emails.append((subject, sender, payload, label))
    return emails

def preprocess_email(email):
    soup = BeautifulSoup(email, "html.parser")
    text = soup.get_text()
    text = re.sub('[^a-zA-Z]', ' ', text).lower()
    return text


phishing_emails = extract_emails('emails-phishing.mbox', 1)  # Label phishing emails as 1
legal_emails = extract_emails('emails-legal.mbox', 0)  # Label non-phishing emails as 0

all_emails = phishing_emails + legal_emails
processed_emails = [(subject, sender, preprocess_email(body), label) for subject, sender, body, label in all_emails]

corpus = [body for subject, sender, body, label in processed_emails]
labels = [label for subject, sender, body, label in processed_emails]

vectorizer = TfidfVectorizer(max_features=1000)
X = vectorizer.fit_transform(corpus)
y = labels

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = MultinomialNB()
model.fit(X_train, y_train)

# Evaluate the model
predictions = model.predict(X_test)
# Save the model to a file
joblib.dump(model, 'phishing_model.pkl')

# Save the vectorizer as well (it's needed for preprocessing new data)
joblib.dump(vectorizer, 'vectorizer.pkl')

print(classification_report(y_test, predictions))