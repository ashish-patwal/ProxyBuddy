import os;
from datetime import datetime
from pytz import timezone
password = os.environ['password']
username = os.environ['username']

URL = "http://45.116.207.79/moodle/login/index.php"

CLNDRURL = "http://45.116.207.79/moodle/calendar/view.php?view=upcoming"

MARKATTENDANCEURL = "http://45.116.207.79/moodle/mod/attendance/attendance.php"

ATTENDANCEURL_REG = (
    "^http://45\.116\.207\.79/moodle/mod/attendance/view\.php\?id=[0-9]*$"
)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
}

params = {
    "logintoken": "Leave this as it is",
    "username": username,
    "password": password,
}


def getTime()->str:
    return datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
   