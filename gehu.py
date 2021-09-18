from bs4 import BeautifulSoup
import sys
import time
import argparse
import requests
from const import URL, params, headers
from util import submitAttendance

while True:
    with requests.Session() as session:
        html = session.get(URL, verify=False, headers=headers)
        soup = BeautifulSoup(html.content, "html5lib")
        params["logintoken"] = soup.find("input", {"name": "logintoken"})["value"]

        html2 = session.post(URL, verify=False, headers=headers, data=params)
        if html2.url == URL:
            print("Wrong Credentials")
        else:
            headers.update(session.cookies.get_dict())
            submitAttendance(session, headers)
            print("done")

        time.sleep(1800)
