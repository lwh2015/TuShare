#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
from django.http import HttpResponse
import pandas as pd
import numpy as np
import tushare as ts


class DateEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o,np.ndarray):
            return  o.tolist()
        return json.JSONEncoder.default(self,o)


def today_all(request):
    data = ts.get_today_all()
    data = pd.DataFrame(data)

    # return HttpResponse('123')
    res = {'columns':['code','name','changepercent','trade','open','high','low','settlement','volume','turnoverratio','amount','per','pb','mktcap','nmc'],'data':json.loads(json.dumps(data.values,cls=DateEncoder))}
    return HttpResponse(json.dumps(res),content_type="application/json")