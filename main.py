#!/usr/bin/env python3

# -*- coding: utf-8 -*-


import sys

from jd_mask_spider_requests import JdMaskSpider
from jdlogger import logger

if __name__ == '__main__':
    a = """
  ________   __    _               __       __  _
 |___  /\ \ / /   | |              \ \     / / | |
    / /  \ V /    | |               \ \   / /  | |
   / /    > < _   | |                \ \ / /   | |
  / /__  / . \ |__| |1.预约商品       \ V /    | |
 /_____|/_/ \_\____/ 2.秒杀抢购商品    \_/     |_|
    """
    logger.info(a)
    start_tool = JdMaskSpider()
    choice_function = input('选择功能:')
    if choice_function == '1':
        start_tool.login_by_QRcode()
        start_tool.make_reserve()
    elif choice_function == '2':
        start_tool.login_by_QRcode()
        start_tool.request_seckill_url()
        start_tool.request_seckill_checkout_page()
        while True:
            try:
                order = start_tool.submit_seckill_order()
                if order:
                    break
            except Exception as e:
                logger.error('提交失败:{0},正在重试...'.format(e))
            else:
                continue
    else:
        print('没有此功能')
        sys.exit(1)
