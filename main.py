import sys
from jd_mask_spider_requests import Jd_Mask_Spider
import platform

if __name__ == '__main__':
    a = """
  ________   __    _               __       __  _
 |___  /\ \ / /   | |              \ \     / / | |
    / /  \ V /    | |               \ \   / /  | |
   / /    > < _   | |                \ \ / /   | |
  / /__  / . \ |__| |1.预约商品       \ V /    | |
 /_____|/_/ \_\____/ 2.秒杀抢购商品    \_/     |_|
    """
    start_tool = Jd_Mask_Spider()
    print(a)
    choice_function = input('选择功能:')
    if choice_function == '1':
        #cookies Login
        #start_tool.login()
        #QRCode Login
        start_tool.login_by_QRcode()
        start_tool.make_reserve()
    elif choice_function == '2':
        start_tool.login_by_QRcode()
        start_tool.request_seckill_url()
        start_tool.request_seckill_checkout_page()
        while True:
            try:
                seckill_order=start_tool.submit_seckill_order()
                if seckill_order == True:
                    break
            except Exception as e:
                print('提交失败正在重试...'+e) 
    else:
        print('没有此功能')
        sys.exit(1)
