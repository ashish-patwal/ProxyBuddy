from urllib.parse import urlparse, parse_qs
from message import sendMessage
from context import RequestURL
from const import getTime
from requests import codes
import re

from const import CLNDRURL, ATTENDANCEURL_REG, MARKATTENDANCEURL

print("PROXY BUDDY IS ONLINE BITCH")

def Links(soup):
    return [
        data.attrs["href"]
        for data in soup.find("div", {"class": "maincalendar"}).find_all(
            "a", href=re.compile(ATTENDANCEURL_REG)
        ]
    )


def submitAttendance(session, headers):
    with RequestURL(CLNDRURL, session, headers) as soup:
        for link in Links(soup):
            # submitAttendance(link, session, headers)
            markAttendance(link, session, headers)


def markAttendance(targetURL, session, headers):

    payload = {
        "submitbutton": "Save+changes",
        "_qf__mod_attendance_student_attendance_form": "1",
        "mform_isexpanded_id_session": "1",
    }

    with RequestURL(targetURL, session, headers) as soup:
        try:
            target = soup.find("a", text="Submit attendance")["href"]
        except TypeError:
            message = "NO Submission Link"
            print(message)
        else:
            for k, v in parse_qs(urlparse(target).query).items():
                payload[k] = "".join(v)
            with RequestURL(target, session, headers) as soup2:
                presentValue = soup2.find("input", {"name": "status", "type": "radio"})[
                    "value"
                ]
                # statusValue = presentValue.find_parent('input',{'name': 'status', 'type': 'radio'}).attrs['value']
                payload.setdefault("status", presentValue)

                r = session.post(
                    MARKATTENDANCEURL, verify=False, headers=headers, data=payload
                )
                if r.status_code == codes["ok"]:
                    print(soup.title.string)
                    print("Submitted Attendance successfully")
                    message = f"{soup.title.string} : {getTime()} : Submitted Attendance Successfully"
                else:
                    message = f"Error happend : {r.status_code}"
                sendMessage(message)
