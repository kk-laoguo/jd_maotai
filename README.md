# Jd_maotai

## 馒头和米粒验证程序可以抢购成功（再此源码基础上增加扫码登录，同步京东服务器时间）

##### 非常感谢原作者 https://github.com/zhou-xiaojun/jd_mask 提供的代码

## 主要功能

- 登陆京东商城（[www.jd.com](http://www.jd.com/)）
  - scanQrCode  登录
  - add sync jd time : python jd_sync_time.py
  - cookies登录 (需要自己手动获取)
- 预约茅台
  - 定时自动预约
- 秒杀预约后等待抢购
  - 定时开始自动抢购

## 运行环境

- [Python 3](https://www.python.org/)

## 第三方库

- 需要使用到的库已经放在requirements.txt，使用pip安装的可以使用指令  
`pip install -r requirements.txt`

## 使用教程  
#### 1. 网页扫码登录
#### 2. 填写config.ini配置信息 
(1)eid,和fp找个普通商品随便下单,然后抓包就能看到,这两个值可以填固定的 
> 不会的话参考原作者的issue https://github.com/zhou-xiaojun/jd_mask/issues/22

(2)sku_id,DEFAULT_USER_AGENT(和cookie获取同一个地方就会看到.直接复制进去就可以了) 
>sku_id我已经按照茅台的填好 

(3)配置一下时间
 
以上都是必填的.

#### 3.运行main.py 
根据提示选择相应功能即可
