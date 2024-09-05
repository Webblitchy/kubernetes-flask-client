from requests import get
from time import sleep

flaskServerUrl = "http://10.30.232.34:8081"


while True:
    try:
        r = get(flaskServerUrl, timeout=1)
        print(r.text)
    except:
        print("Server unreachable")

    sleep(60)