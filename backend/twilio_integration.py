# twilio_integration.py

import os

from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
# Load Twilio credentials from environment variables
ACCOUNT_SID = os.environ.get('ACCOUNT_SID')
AUTH_TOKEN = os.environ.get('AUTH_TOKEN')
FROM = os.environ.get('TWILIO_PHONE_NUMBER')

# Twilio client setup
client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_whatsapp_message(sender_id, message):
    try:
        response = client.messages.create(
            body=message,
            from_=FROM,
            to=f'whatsapp:+{sender_id}'
        )
        return response
    except Exception as e:
        print(f"Error sending message: {e}")
        return None
