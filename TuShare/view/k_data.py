#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import numpy as np
import tushare as ts


class DateEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o,np.ndarray):
            return  o.tolist()
        return json.JSONEncoder.default(self,o)

@csrf_exempt
def k_data(request):
   
    code = request.POST.get('code','')#必填
    ktype = request.POST.get('ktype','D')#选填 默认D
    autype = request.POST.get('autype', 'qfq')#选填 默认 qfq
    def str_to_bool(str):
        return True if str.lower() == 'true' else False
    index = str_to_bool(request.POST.get('index','false'))
    start = request.POST.get('start', '')#选填 默认当前日期
    end = request.POST.get('end', '')#选填 默认当前日期
    k = ts.get_k_data(code,start,end,ktype,autype,index)
    k = pd.DataFrame(k)
    res = {'columns':['date','open','close','high','low','volume','code'],'data':json.loads(json.dumps(k.values,cls=DateEncoder))}
    return HttpResponse(json.dumps(res),content_type="application/json")


