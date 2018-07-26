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
def tick_data(request):

    code = request.POST.get('code','')#必填
    date = request.POST.get('date','')#必填
    src = request.POST.get('src','sn')#选填
    data = ts.get_tick_data(code,date)
    data = pd.DataFrame(data)
    res = {'columns':['time','price','change','volume','amount','type'],'data':json.loads(json.dumps(data.values,cls=DateEncoder))}
    return HttpResponse(json.dumps(res),content_type="application/json")