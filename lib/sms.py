from twilio.rest import TwilioRestClient
import settings

def send(to, message):
    client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(to=to, from_=settings.TWILIO_NUMBER, body=message)