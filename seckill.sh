#!/bin/bash
rm -fr ./cookies
rm -f QRcode.png
rm -f ./jdBuyMask.log

#sync jd time root
#python3 ./jd_sync_time.py
python3 ./main.py
