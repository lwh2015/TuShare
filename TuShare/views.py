from django.shortcuts import render
from dwebsocket.decorators import accept_websocket,require_websocket
from collections import defaultdict
from django.http import HttpResponse
# 保存所有接入的用户地址
allconn = defaultdict(list)
@accept_websocket
def echo(request, userid):
    allresult = {}
    # 获取用户信息
    userinfo = request.user
    allresult['userinfo'] = userinfo
    # 声明全局变量
    global allconn
    if not request.is_websocket():#判断是不是websocket连接
        try:#如果是普通的http方法
            message = request.GET['message']
            return HttpResponse(message)
        except:
            return False
    else:
        # 将链接(请求？)存入全局字典中
        allconn[str(userid)] = request.websocket
       # 遍历请求地址中的消息
        for message in request.websocket:
            # 将信息发至自己的聊天框
            request.websocket.send(message)
            # 将信息发至其他所有用户的聊天框
            for i in allconn:
                if i != str(userid):
                    allconn[i].send(message)