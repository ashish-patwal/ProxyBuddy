from flask import Flask, send_file, request
from threading import Thread

app = Flask('')


@app.route('/',methods = ['POST', 'GET'])
def main():
    if request.method == 'POST':
      return send_file('./responce.xml')
    else:
      return "PROXY BUDDY NEVER DIES"

def run():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    server = Thread(target=run)
    server.start()
