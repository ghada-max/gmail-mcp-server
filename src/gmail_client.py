import base64
import logging
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from src.config import get_settings

logger = logging.getLogger("gmail_client")
settings = get_settings()

def get_gmail_service():
    """Builds and returns an authorized Gmail API service client."""
    creds = Credentials(
        token=None, 
        refresh_token=settings.google_refresh_token,
        client_id=settings.google_client_id,
        client_secret=settings.google_client_secret,
        token_uri="https://oauth2.googleapis.com/token",
    )
    return build("gmail", "v1", credentials=creds)

def send_real_email(recipient: str, message: str) -> str:
    """Constructs a MIME email and sends it via the official Gmail API."""
    try:
        service = get_gmail_service()
        
        # Build the message
        mime_message = MIMEText(message)
        mime_message["To"] = recipient
        mime_message["Subject"] = "message from AI assistant"  
        
        # Encode for Google API (base64url)
        raw_bytes = mime_message.as_bytes()
        raw_string = base64.urlsafe_b64encode(raw_bytes).decode("utf-8")
        body = {"raw": raw_string}
        
        # Send via Google API
        sent_message = service.users().messages().send(userId="me", body=body).execute()
        
        logger.info(f"Email successfully sent. ID: {sent_message.get('id')}")
        return f"SUCCESS: Email successfully sent to {recipient}."
        
    except Exception as e:
        logger.error(f"Failed to send email: {str(e)}")
        raise RuntimeError(f"Secure email transmission failed: {str(e)}")