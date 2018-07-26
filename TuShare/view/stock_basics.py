# -*- coding: UTF-8 -*-
import json

from django.http import HttpResponse

import tushare as ts

from .publiceClass import DateEncoder

def stock_basics(request):
    try:
        data = ts.get_stock_basics()
        res = {'columns':[
            '代码',
            '名称',
            '所属行业',
            '地区',
            '市盈率',
            '流通股本(亿)',
            '总股本(亿)',
            '总资产(万)',
            '流动资产',
            '固定资产',
            '公积金',
            '每股公积金',
            '每股收益',
            '每股净资',
            '市净率',
            '上市日期',
            '未分利润',
            '每股未分配',
            '收入同比(%)',
            '利润同比(%)',
            '毛利率(%)',
            '净利润率(%)',
            '股东人数'
        ],'data':json.loads(json.dumps(data.values,cls=DateEncoder))}
    except(Exception):
        return HttpResponse(Exception)
    else:
        return HttpResponse(json.dumps(res),content_type="application/json")
