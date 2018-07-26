# -*- coding: UTF-8 -*-
import json

from django.http import HttpResponse

import tushare as ts

from .publiceClass import DateEncoder

def st_classified(request):
    try:
        data = ts.get_st_classified()

        res = {'columns':[
            '股票代码',
            '股票名称',
        ],'data':json.loads(json.dumps(data.values,cls=DateEncoder))}
    except(KeyError):
        return HttpResponse(KeyError)
    else:
        return HttpResponse(json.dumps(res),content_type="application/json")