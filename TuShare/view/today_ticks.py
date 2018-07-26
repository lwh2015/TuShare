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
def today_ticks(request):
    code = request.POST.get('code','')#必填
    data = ts.get_today_ticks(code)
    res = {'columns':[
        'time',
        'price',
        'pchange',
        'change',
        'volume',
        'amount',
        'type'
    ],'data':json.loads(json.dumps(data.values,cls=DateEncoder))}
    return HttpResponse(json.dumps(res),content_type="application/json")