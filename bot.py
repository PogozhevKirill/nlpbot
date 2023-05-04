import json
import logging

from aiohttp import web, ClientSession

from cfg.config import TELEGRAM_TOKEN, TELEGRAM_WEBHOOK, ADMIN_MODE, ADMIN_CHAT_ID
from middlewares.middleware import middleware_debug_admin
from handlers.handlers import message_handle


API_URL = 'https://api.telegram.org/bot%s/sendMessage' % TELEGRAM_TOKEN
headers = {
    'Content-Type': 'application/json'
}


async def handler(request):
    data = await request.json()
    logging.info(str(data))
    message = await message_handle(data)
    if message['text'] is not None:
        async with ClientSession() as session:
            async with session.post(API_URL,
                                    data=json.dumps(message),
                                    headers=headers) as resp:
                try:
                    assert resp.status == 200
                except:
                    return web.Response(status=500)
    return web.Response(status=200)


async def bot():
    logging.basicConfig(level=logging.DEBUG)
    app = web.Application(middlewares=[])
    app.router.add_post(TELEGRAM_WEBHOOK, handler)
    # if ADMIN_MODE:
    #     app.middlewares.append(middleware_debug_admin)

    message = {
        'chat_id': ADMIN_CHAT_ID,
        'text': 'Bot successfully started!'
    }
    logging.warning("API_URL: {}".format(API_URL))
    logging.warning("message: {}".format(json.dumps(message)))
    async with ClientSession() as session:
        async with session.post(API_URL,
                                data=json.dumps(message),
                                headers=headers) as resp:
            try:
                assert resp.status == 200
            except:
                logging.warning("Could not sent start message")
    logging.info("post added")
    return app
