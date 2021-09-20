import os
from twilio.rest import Client

phno = os.environ['phno']
twilioNum = os.environ['twilioNum']
authtoken = os.environ['authtoken']
acc_sid = os.environ['account_sid']

account_sid = acc_sid
auth_token = authtoken
client = Client(account_sid, auth_token)

def sendMessage(message: str):
    message = client.messages.create(
        from_=twilioNum,
        body=message,
        to=phno,
    )
