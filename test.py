import urllib.request
import json
import datetime
import random
import string
import time
import os
import requests
import prx

os.system('cls' if os.name == 'nt' else 'clear')
print("[-] With this script, you can getting unlimited GB on Warp+.")
print("Original script was made by ALIILAPRO, site: aliilapro.github.io")

referrer = input("[#] Enter the WARP+ ID: ")
referrer = "c6ce47df-d95b-4b35-a2a7-49a0e9d0b248"


def genString(stringLength):
    try:
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for i in range(stringLength))
    except Exception as error:
        print(error)


def digitString(stringLength):
    try:
        digit = string.digits
        return ''.join((random.choice(digit) for i in range(stringLength)))
    except Exception as error:
        print(error)


url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'


def run():
    try:
        install_id = genString(22)
        body = {"key": "{}=".format(genString(43)),
                "install_id": install_id,
                "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
                "referrer": referrer,
                "warp_enabled": False,
                "tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
                "type": "Android",
                        "locale": "en_US"}
        data = json.dumps(body).encode('utf8')
        headers = {'Content-Type': 'application/json; charset=UTF-8',
                   'Host': 'api.cloudflareclient.com',
                   'Connection': 'Keep-Alive',
                   'Accept-Encoding': 'gzip',
                   'User-Agent': 'okhttp/3.12.1'
                   }
        response = requests.get(
            url=url, data=data, headers=headers, proxies=proxydic[0])
        print(response.headers)
        print("")
        print(response.json)
        return 200
    except Exception as error:
        raise


with open('proxies.json') as f:
    proxydic = json.load(f)
g = 0
b = 0
waitnum = 55

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"[-] WORK ON ID: {referrer}")
    result = run()
    print(result)
    if result == 200:
        g = g + 1
    else:
        b = b + 1
        print("[:(] Error when connecting to server.")
        time.sleep(5)
    print(data)
