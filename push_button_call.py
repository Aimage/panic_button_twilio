# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
import RPi.GPIO as GPIO

RELATIVE_NUMBERS = [""]
ORGINATE_NUMBER = "+15017122661"

HELP_TEXT = "Please help!! I have an emergency problem!"

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']


def call_relative(client, relaive_number):
    call = client.calls.create(
        twiml=f'<Response><Say>{HELP_TEXT}</Say></Response>',
        to=relaive_number,
        from_=ORGINATE_NUMBER)
    print(call.sid)
    return call


def call_for_help(channel):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    for relative_number in RELATIVE_NUMBERS:
        call_relative(client, relative_number)


GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
GPIO.setup(
    10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN
)  # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(10, GPIO.RISING, callback=call_for_help)
