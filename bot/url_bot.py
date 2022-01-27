# -*- coding: utf-8 -*-
import json

from sanic import Blueprint
from sanic.views import HTTPMethodView
from sanic.response import json as resjson
from skpy import Skype
import requests
from bot.variable import *

url_bot = Blueprint('url_bot', url_prefix='/skype')


async def sent_msg_tele(msg):
    try:

        bot_token = '5186109565:AAESHiHEMGKp5G1U36x4FAVumBaWkTfKJSI'
        chat_id = '1389974666'
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chat_id + '&text=' + msg
        response = requests.get(send_text, timeout=2)
        return resjson({'result': response.get('ok', 'false'), 'msg': ''})
    except Exception as ex:
        return resjson({'result': '0', 'msg': ex})


class Bot(HTTPMethodView):
    async def post(self, req, **kwargs):
        return await sent_msg_tele(req.json['msg'])


url_bot.add_route(Bot.as_view(), '/ping', methods=['POST'])
