import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import tushare as ts
from .publiceClass import DateEncoder

@csrf_exempt
def profit_data(request):

    try:
        year = request.POST.get('year', 2014)  # 选填
        top = request.POST.get('top', 25)  # 选填
        data = ts.profit_data(int(year), int(top))


        res = {'columns': [
            'code',
            'name',
            'year',
            'report_date',
            'divi',
            'shares'
        ], 'data': json.loads(json.dumps(data.values, cls=DateEncoder))}
    except(TypeError):
        return HttpResponse(TypeError)
    else:
        return HttpResponse(json.dumps(res),content_type="application/json")


