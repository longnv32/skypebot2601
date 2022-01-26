import aiohttp
from sanic import Sanic
from bot.url_bot import url_bot
import json as json
arrs = []
app = Sanic(__name__)
app.config.KEEP_ALIVE = False
app.blueprint(url_bot)


@app.listener('before_server_start')
async def set_up_db(app, loop):
    app.REQ_SESSION = aiohttp.ClientSession(loop=loop)


@app.listener('after_server_stop')
async def close_up_db(app, loop):
    await app.REQ_SESSION.close()


@app.middleware('response')
async def halt_response(req, res):
    print(str(res.body, 'utf-8'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000, workers=1, debug=False)