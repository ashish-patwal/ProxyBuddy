import keep_alive
from bs4 import BeautifulSoup
import time
import requests
from const import URL, params, headers, getTime
from util import submitAttendance

def run():
    with requests.Session() as session:
        html = session.get(URL, verify=False, headers=headers)
        soup = BeautifulSoup(html.content, "html5lib")
        params["logintoken"] = soup.find("input",
                                         {"name": "logintoken"})["value"]

        html2 = session.post(URL, verify=False, headers=headers, data=params)
        if html2.url == URL:
            print("Wrong Credentials")
        else:
            headers.update(session.cookies.get_dict())
            print(getTime())
            submitAttendance(session, headers)

keep_alive.keep_alive()

while True:
  run()
  time.sleep(1800)