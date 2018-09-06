#!/usr/bin/env python


import sys
sys.path.insert(0, '../')

import os
if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'demo.settings'

 # 让django进行初始化设置
import django
django.setup()


from spider_data.models import Data
import json
def create_model(Data):
    with open('../../first_spider/shop_data.json','r') as f:
        shop_data = f.read()
        print(shop_data)
        # 将json数据转化成列表
        shop_data = json.loads(shop_data)
        for  data  in  shop_data:
            Data.objects.create(
                shop_name=data['shop_name'],
                shop_addr=data['shop_addr'],
                aver_price=data['aver_price'],
                shop_star=data['shop_star'],
                comment_count=data['comment_count'],
            )

if __name__ == '__main__':
    create_model(Data)



