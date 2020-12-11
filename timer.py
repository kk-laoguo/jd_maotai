#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import json
import time
from datetime import datetime

import requests

from config import global_config
from jdlogger import logger


class Timer(object):
    def __init__(self, sleep_interval=0.0001):
        # '2018-09-28 22:45:50.000'
        self.buy_time = datetime.strptime(global_config.getRaw(
            'config', 'buy_time'), "%Y-%m-%d %H:%M:%S.%f")
        self.sleep_interval = sleep_interval

    @staticmethod
    def getTime():
        url = 'https://a.jd.com//ajax/queryServerData.html'
        ret = requests.get(url).text
        js = json.loads(ret)
        return float(js.get('serverTime') / 1000)

    def start(self):
        logger.info('正在等待到达设定时间:%s' % self.buy_time)
        now_time_local = datetime.now
        while True:
            now_time = datetime.fromtimestamp(self.getTime())
            if now_time >= self.buy_time or now_time_local() >= self.buy_time:
                logger.info('时间到达，开始执行……')
                break
            else:
                time.sleep(self.sleep_interval)
