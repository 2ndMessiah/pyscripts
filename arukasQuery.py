# coding=utf-8
''' 
Arukas will randomly restart the apps that exceed the usage limitations set for free accounts, after which the app's service port and ip will be changed.
This script helps to retrieve arukas app's ip and port, and forward to serverChan(http://sc.ftqq.com/).
Since app.arukas.io is blocked, one might as deploy this in a VPS and use cron or any scheduled tasking mechanism to poll the info.
Fill in the parameters in the header first.
'''

import requests as r
import os

#parameters 
apiID=apiID
apikey=apikey
portorder=-1
serverchanaddr=serverchanaddr



while True:
    try:
        a=r.get('https://app.arukas.io/api/apps',auth=(apiID,apikey))
        c = a.json()['included'][0]['attributes']['port-mappings'][0][portorder]
        break
    except:
        continue

addr='{}:{}'.format(c['host'],c['service-port'])
if os.path.exists('./arukas.txt'):
    f=open('arukas.txt','r+')
    if f.readline() !=addr:
        response = r.get(serverchanaddr,
                         {'text': 'ARUKAS ALARM', 'desp': '{}:{}'.format(c['host'], c['service-port'])})
        f.truncate()
        f.write(addr)
    f.close()
else:
    f = open('arukas.txt', 'a+')
    f.write(addr)
    f.close()
    response = r.get(aerverchanaddr,
                     {'text': 'ARUKAS ALARM', 'desp': '{}:{}'.format(c['host'], c['service-port'])})




