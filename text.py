from twilio.rest import Client
import config


client = Client(config.account_sid, config.auth_token)

call = client.messages.create(
  to = config.phone_number,
  from_ = config.twilio_phone_number,
  body = "The test sms from twilio to my phone through python project."
)

sms = call.date_created
print(f"The message has been sent on {sms}")
