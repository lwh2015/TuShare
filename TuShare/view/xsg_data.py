import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import tushare as ts
from .publiceClass import DateEncoder

@csrf_exempt
def xsg_data(request):
    try:
        year = request.POST.get('year', '')  # 必填
        month = request.POST.get('month', '')  # 必填
        data = ts.xsg_data(year,month)
        res = {'columns':[
            'code',
            'name',
            'date',
            'count',
            'ratio'
        ],'data':json.loads(json.dumps(data.values,cls=DateEncoder))}
    except(BaseException):
        return HttpResponse(BaseException)
    else:
        return HttpResponse(json.dumps(res),content_type="application/json")