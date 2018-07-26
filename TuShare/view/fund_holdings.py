import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import tushare as ts
from .publiceClass import DateEncoder

@csrf_exempt
def fund_holdings(request):
    try:
        year = request.POST.get('year', '')  # 必填
        quarter = request.POST.get('quarter', '')  # 必填
        data = ts.fund_holdings(year,quarter)
        res = {'columns':[
            'code',
            'name',
            'date',
            'nums',
            'nlast',
            'count',
            'clast',
            'amount',
            'ratio'
        ],'data':json.loads(json.dumps(data.values,cls=DateEncoder))}
    except(BaseException):
        return HttpResponse(BaseException)
    else:
        return HttpResponse(json.dumps(res),content_type="application/json")