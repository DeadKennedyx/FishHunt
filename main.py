from googleapiclient.discovery import build
import auth
import phishing_detection

def main():
    creds = auth.gmail_authenticate()
    service = build('gmail', 'v1', credentials=creds)
    phishing_detection.check_phishing(service)

if __name__ == '__main__':
    main()