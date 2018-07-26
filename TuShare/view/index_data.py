import json
from django.http import HttpResponse
import numpy as np
import tushare as ts
from .publiceClass import DateEncoder

def index_data(request):
    data = ts.get_index()
    
    res = {'columns':[
        'code',
        'name',
        'change',
        'open',
        'preclose',
        'close',
        'high',
        'low',
        'volume',
        'amount'
    ],'data':json.loads(json.dumps(data.values,cls=DateEncoder))}
    return HttpResponse(json.dumps(res),content_type="application/json")