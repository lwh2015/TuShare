# -*- coding: UTF-8 -*-
import json
import math
from django.http import HttpResponse
import numpy as np
import tushare as ts

from .publiceClass import DateEncoder

def new_stocks(request):

    try:
        data = ts.new_stocks()
        stocksData = np.array(data.values)
        for i in range(len(stocksData)):
           for x in range(len(stocksData[i])):

               if isinstance(stocksData[i][x],float):
                    if math.isnan(stocksData[i][x]):
                        stocksData[i][x] = 0
                        
        res = {"columns":[
            'code',
            'name',
            'ipo_date',
            'issue_date',
            'amount',
            'markets',
            'price',
            'pe',
            'limit',
            'funds',
            'ballot'
        ],"data":json.loads(json.dumps(stocksData,cls=DateEncoder))}


    except(BaseException):
        return HttpResponse(BaseException)
    else:
        return HttpResponse(json.dumps(res),content_type="application/json")