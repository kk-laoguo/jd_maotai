#!/usr/bin/env python3

# -*- coding: utf-8 -*-


'''
    京东时间同步for windows
    需要安装win32api和requests
    pip install pypiwin32
    pip install requests
'''
import json
import os
from datetime import datetime
import requests



def getTime():
    url = 'https://a.jd.com//ajax/queryServerData.html'
    ret = requests.get(url).text
    js = json.loads(ret)
    return float(js.get('serverTime') / 1000)


def setSystemTime():
    strTime = datetime.strftime(datetime.fromtimestamp(
        getTime() + 1), '%Y-%m-%d %H:%M:%S')
    command = 'date -s "{}"'.format(strTime)
    os.system(command)
    print(command)

if __name__ == '__main__':
    #setSystemTime()  #运行一次后，在本条语句前加#注释后可以查看时间同步情况
    for num in range(0, 10):
        print("京东时间%s:%s\n本地时间%s:%s" %
              (num, datetime.fromtimestamp(getTime()), num, datetime.now()))
