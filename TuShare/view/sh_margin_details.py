# -*- coding: UTF-8 -*-
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import tushare as ts
from .publiceClass import DateEncoder

@csrf_exempt
def sh_margin_details(request):
    try:
        date = request.POST.get('date','')
        symbol = request.POST.get('symbol','')
        start = request.POST.get('start','')
        end = request.POST.get('end','')

        data = ts.sh_margin_details(start,end,symbol)
        res = {'columns':[
            '信用交易日期',
            '标的证券代码',
            '标的证券简称',
            '本日融资余额(元)',
            '本日融资买入额(元)',
            '本日融资偿还额(元)',
            '本日融券余量',
            '本日融券卖出量',
            '本日融券偿还量',
        ],'data':json.loads(json.dumps(data.values,cls=DateEncoder))}
    except(BaseException):
        return HttpResponse(BaseException)
    else:
        return HttpResponse(json.dumps(res),content_type="application/json")