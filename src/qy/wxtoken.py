#!/usr/bin/python
import hashlib
import json
import time

import requests

from src.utils import grandom

APP_ID = "ww87177eb4b3409ec5"

SECRET = "fPsN8NpnK1wsG8wKIibxa6E-txSw-iVDc2SJoNi-T3A"

GET_ACCESS_TOKEN = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}".format(corpid=APP_ID, corpsecret=SECRET)

r = requests.get(GET_ACCESS_TOKEN)

print(r.text)

data = json.loads(r.text)

access_token = data['access_token']

print(access_token)

GET_TICKET = "https://qyapi.weixin.qq.com/cgi-bin/get_jsapi_ticket?access_token={ACCESS_TOKE}".\
    format(ACCESS_TOKE=access_token)

r = requests.get(GET_TICKET)

print(r.text)

data = json.loads(r.text)

jsapi_ticket = data['ticket']

print("jsapi_ticket", jsapi_ticket)

noncestr = grandom.generate_random_str(16)

print("noncestr: ", noncestr)

timestamp = int(time.time())

print("timestamp: ", timestamp)

url = ""

str1 = "jsapi_ticket={JSAPITICKET}&noncestr=" \
       "{NONCESTR}&timestamp={TIMESTAMP}&url={URL}".format(JSAPITICKET=jsapi_ticket,
                                                                                               NONCESTR=noncestr,
                                                                                               TIMESTAMP=timestamp,
                                                                                               URL=url)

print("str1: ", str1)

sha1 = hashlib.sha1()

sha1.update(str1.encode('utf-8'))

signature = sha1.hexdigest()

print("signature:", signature)


