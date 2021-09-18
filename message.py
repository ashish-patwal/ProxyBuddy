import os
from twilio.rest import Client

phno = os.environ['phno']

msg_sid = os.environ['messaging_service_sid']

authtoken = os.environ['authtoken']

acc_sid = os.environ['account_sid']


def sendMessage(message: str):
    account_sid = acc_sid
    auth_token = authtoken
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        messaging_service_sid=msg_sid,
        body=message,
        to=phno,
    )
