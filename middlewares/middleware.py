from aiohttp import web

from cfg.config import ADMIN_CHAT_ID


async def middleware_debug_admin(app, handler):
    async def middleware_handler(request):
        data = await request.json()
        if data['message']['from']['id'] != ADMIN_CHAT_ID:
            return web.Response(status=200)
        return await handler(request)
    return middleware_handler


# async def middleware_message_send(app, handler):
#     async def middleware_handler(request):
#         data = await request.json()
#         if data['message']['from']['id'] in black_list:
#             return web.Response(status=200)
#         return await handler(request)
#     return middleware_handler
