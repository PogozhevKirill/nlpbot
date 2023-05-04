import json

from db.mongo import users, do_find_one, do_insert_one, do_find_many, do_delete_one


async def enter_username(data: dict):
    current_char = await do_find_one({'_id': data['message']['chat']['id']}, users)
    if current_char is None:
        await do_insert_one({'_id': data['message']['chat']['id'],
                             'name': data['message']['text']}, users)
        return 'Персонаж **{}** успешно создан!'.format(data['message']['text'])
    return None


async def get_users_list():
    users_list = await do_find_many({}, users)
    return str(users_list)


async def delete_user(data: dict):
    current_char = await do_find_one({'_id': data['message']['chat']['id']}, users)
    if current_char is not None:
        await do_delete_one({'_id': data['message']['chat']['id']}, users)
        return 'Персонаж **{}** успешно удален!'.format(current_char['name'])
    else:
        return 'Вы еще не создали персонажа. Чтобы начать используйте /start'


async def message_handle(data: dict) -> dict:
    command = data['message']['text']
    message = {
        'chat_id': data['message']['chat']['id'],
        'text': None
    }

    # /start
    if command == '/start':
        message['text'] = await enter_username(data)
    if command == '/get_users':
        message['text'] = await get_users_list()
    if command == '/delete_user':
        message['text'] = await delete_user(data)

    return message
