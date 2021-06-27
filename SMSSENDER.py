from twilio.rest import Client
#  I HAVE HIDDEN THE INFORMATION LIKE NUMBERS AND TOKENS FOR SECURITY REASONS
account_sid = '************************'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='***********************',
    body='I CANT BELIEVE THIS WORKS',
    to='+1000000000000000000'
)

print(message.sid)