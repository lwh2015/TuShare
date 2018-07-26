# -*- coding: UTF-8 -*-
import json

from django.http import HttpResponse

import tushare as ts

from .publiceClass import DateEncoder

def concept_classified(request):
    try:
        data = ts.get_concept_classified()
        res = {'columns':[
            '股票代码',
            '股票名称',
            '概念名称'
        ],'data':json.loads(json.dumps(data.values,cls=DateEncoder))}
    except(BaseException):
        return HttpResponse(BaseException)
    else:
        return HttpResponse(json.dumps(res),content_type="application/json")