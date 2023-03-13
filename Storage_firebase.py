import pyrebase
import datetime, pytz
import requests, json
import urllib.parse

tz = pytz.timezone('Asia/Bangkok')

def getDate():
    now1 = datetime.datetime.now(tz)
    month_name = 'x มกราคม กุมภาพันธ์ มีนาคม เมษายน พฤษภาคม มิถุนายน กรกฎาคม สิงหาคม กันยายน ตุลาคม พฤศจิกายน ธันวาคม'.split()[now1.month]
    thai_year = now1.year + 543
    return "%d %s %d"%(now1.day, month_name, thai_year) # 30 ตุลาคม 2560 20:45:30

def getTime():
    now1 = datetime.datetime.now(tz)
    time_str = now1.strftime('%H:%M:%S')
    return "%s"%(time_str)

def send2firebase(n, status, count):
    #database.drop
    config = {"apiKey": "AIzaSyDpKMaOJgpnkMuY2D5PCQqO3gyK2oaqbCA",
              "authDomain": "testfirebase2-75552.firebaseapp.com",
              "databaseURL": "https://testfirebase2-75552-default-rtdb.firebaseio.com",
              "projectId": "testfirebase2-75552",
              "storageBucket": "testfirebase2-75552.appspot.com",
              "messagingSenderId": "135365186638",
              "appId": "1:135365186638:web:39465af4b367cba9cc9f1f",
              "measurementId": "G-D27GGT5NFP"}

    firebase = pyrebase.initialize_app(config)
    #storage = firebase.storage()
    database = firebase.database()
    data = {"Date":getDate(), "Time":getTime(), "n":n, "Status":status}
    database.child("Status").push(data)
    if(count >= 100):
        database.child("Status").remove()

def sendNotification(n):
    LINE_ACCESS_TOKEN="pLrbaK7vDl2zF4wo45yywogkZDThZCy20cUwAc8spc5"
    url = "https://notify-api.line.me/api/notify"

    message = "หมูตัวที่ ",n,"เปลี่ยนสถานะ" # ข้อความที่ต้องการส่ง
    msg = urllib.parse.urlencode({"message":message})
    LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
    session = requests.Session()
    a=session.post(url, headers=LINE_HEADERS, data=msg)
    print(a.text)