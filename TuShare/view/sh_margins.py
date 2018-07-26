# -*- coding: UTF-8 -*-
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import tushare as ts
from .publiceClass import DateEncoder

@csrf_exempt
def sh_margins(request):
    try:
        start = request.POST.get('start','')#选填
        end = request.POST.get('end','')#选填
        data = ts.sh_margins(start,end)
        res = {'columns':[
            '信用交易日期',
            '本日融资余额(元)',
            '本日融资买入额(元)',
            '本日融券余量',
            '本日融券余量金额(元)',
            '本日融券卖出量',
            '本日融资融券余额(元)'
        ],'data':json.loads(json.dumps(data.values,cls=DateEncoder))}
    except(BaseException):
        return HttpResponse(BaseException)
    else:

        return HttpResponse(json.dumps(res),content_type="application/json")

