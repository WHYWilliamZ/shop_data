#!/usr/bin/env python

from spider_data.models import Data
import sys
sys.path.insert(0, '../')

import os
if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'demo.settings'

 # 让django进行初始化设置
import django
django.setup()


data = [{'name':'张三','addr':'北京','phone':'18833028602'},{'name':'李四','addr':'上海','phone':'18833028603'}]

def create_model(data,Data):
    for  dat  in  data:
        Data.objects.create(
            name=dat['name'],
            addr=dat['addr'],
            phone=dat['phone']
        )

if __name__ == '__main__':
    create_model(data,Data)



