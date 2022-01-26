# -*- coding: utf-8 -*-
import json

from sanic import Blueprint
from sanic.views import HTTPMethodView
from sanic.response import json as resjson
from skpy import Skype
from bot.variable import *

url_bot = Blueprint('url_bot', url_prefix='/skype')
user = Skype('n13dccn109@student.ptithcm.edu.vn', 'longboy123')
lischat = []
lst=user.chats
user.chats.recent()
for i in lst:
    try:
        item = {"channelname":str(i.topic).lower(),"value":i.id}
        lischat.append(item)
    except:
        pass


async def sent_msg(msg,channel):
    try:
        for channels in lischat:
            if(channels['channelname']==str(channel).lower()):
                idchannel = channels['value']
        chat = user.chats.chat(idchannel)
        mes = json.dumps(msg,ensure_ascii=False).encode('utf8').decode()
        str(mes).replace('\\n','\n')
        if mes[-1] == '"':
            chat.sendMsg(mes[1:-1])
        else:
            chat.sendMsg(mes)
        return resjson({'result': '1', 'msg': ''})
    except Exception as ex:
        return resjson({'result': '0', 'msg': str(ex)})


async def sent_msg_oldversion(msg):
    try:
        chat = user.chats.chat('19:3979e87e4cf5406d9323adf911845649@thread.skype')
        mes = json.dumps(msg,ensure_ascii=False).encode('utf8').decode()
        chat.sendMsg(str(mes).replace('\\n','\n'))
        return resjson({'result': '1', 'msg': ''})
    except Exception as ex:
        return resjson({'result': '0', 'msg': ex})


class Bot(HTTPMethodView):
    async def get(self, req):
        js = {'result': '1'}
        return resjson(js)


class SentMsg(HTTPMethodView):
    async def post(self, req, **kwargs):
        if(req.json.get('channel')==None):
            return await sent_msg_oldversion(req.json['msg'])
        return await sent_msg(req.json['msg'],req.json['channel'])


url_bot.add_route(SentMsg.as_view(), '/bot', methods=['POST'])
url_bot.add_route(Bot.as_view(), '/ping')
