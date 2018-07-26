# -*- coding: UTF-8 -*-
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import tushare as ts
from .publiceClass import DateEncoder

@csrf_exempt
def sz_margin_details(request):
    try:
        date = request.POST.get('date','')
        data = ts.sz_margin_details(date)
        res = {'columns':[
            '标的证券代码',
            '标的证券简称',
            '融资买入额(元)',
            '融资余额(元)',
            '融券卖出量',
            '融券余量',
            '融券余量(元)',
            '融资融券余额(元)',
            '信用交易日期',
        ],'data':json.loads(json.dumps(data.values,cls=DateEncoder))}
    except(BaseException):
        return HttpResponse(BaseException)
    else:
        return HttpResponse(json.dumps(res),content_type="application/json")