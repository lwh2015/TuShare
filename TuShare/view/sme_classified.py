# -*- coding: UTF-8 -*-
import json

from django.http import HttpResponse

import tushare as ts

from .publiceClass import DateEncoder

def sme_classified(request):
    try:
        data = ts.get_sme_classified()

        res = {'columns':[
            '股票代码',
            '股票名称',
        ],'data':json.loads(json.dumps(data.values,cls=DateEncoder))}
    except(Exception):
        return HttpResponse('error',Exception)
    else:
        return HttpResponse(json.dumps(res),content_type="application/json")