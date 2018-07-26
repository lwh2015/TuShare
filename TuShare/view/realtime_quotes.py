import json
from django.http import HttpResponse
from dwebsocket import accept_websocket
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
def realtime_quotes(request):
    code = request.POST.get('code','')#必填

    data = ts.get_realtime_quotes(eval(code))
    # data = pd.DataFrame(data)
    # print(data.values)
    res = {'columns':[
        'name',
        'pre_close',
        'price',
        'high',
        'low',
        'bid',
        'ask',
        'volumn',
        'amount',
        'b1_v',
        'b1_p',
        'b2_v',
        'b2_p',
        'b3_v',
        'b3_p',
        'b4_v',
        'b4_p',
        'b5_v',
        'b5_p',
        'a1_v',
        'a1_p',
        'a2_v',
        'a2_p',
        'a3_v',
        'a3_p',
        'a4_v',
        'a4_p',
        'a5_v',
        'a5_p',
        'date',
        'time'
    ],'data':json.loads(json.dumps(data.values,cls=DateEncoder))}
    return HttpResponse(json.dumps(res),content_type="application/json")

@accept_websocket
def socket_realtime_quotes(request):
    message = request.websocket.wait()
    request.websocket.send(message)
