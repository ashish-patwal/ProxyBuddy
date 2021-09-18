from twilio.rest import Client


def sendMessage(message: str):
    account_sid = ""
    auth_token = ""
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        messaging_service_sid="",
        body=message,
        to="",
    )
