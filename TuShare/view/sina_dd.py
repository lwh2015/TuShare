import json
from django.http import HttpResponse,HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import tushare as ts
from .publiceClass import DateEncoder

@csrf_exempt
def sina_dd(request):

    try:
        code = request.POST.get('code', '')  # 必填
        date = request.POST.get('date', '')  # 必填
        vol = request.POST.get('vol', 400)  # 选填
        data = ts.get_sina_dd(code, date, vol)
        # print(data)
        res = {'columns': [
            'code',
            'name',
            'time',
            'price',
            'volume',
            'preprice',
            'type'
        ], 'data': json.loads(json.dumps(data.values, cls=DateEncoder))}
        # return HttpResponse(json.dumps(res), content_type="application/json")
    except(AttributeError):
        return HttpResponseServerError(AttributeError)
    else:
        return HttpResponse(json.dumps(res), content_type="application/json")
