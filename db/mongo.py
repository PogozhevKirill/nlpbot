import motor.motor_asyncio
import logging

from cfg.config import MONGO_URL


client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
mongo_db = client['arcanerealms']
mongo_users = db['users']


async def do_insert_one(document: dict, collection: motor.motor_asyncio.AsyncIOMotorCollection) -> None:
    result = await collection.insert_one(document)
    logging.info('MongoDB insert one: result {}'.format(repr(result.inserted_id)))
    return


async def do_find_one(filter_dict: dict, collection: motor.motor_asyncio.AsyncIOMotorCollection) -> dict:
    document = await collection.find_one(filter_dict)
    logging.info('MongoDB find one: result {}'.format(repr(document)))
    return document


async def do_find_many(filter_dict: dict, collection: motor.motor_asyncio.AsyncIOMotorCollection, length=10) -> list:
    cursor = collection.find(filter_dict)
    output = []
    for doc in await cursor.to_list(length):
        output = output + [doc]
    logging.info('MongoDB find many: {} filter {}'.format(len(output), filter_dict))
    return output


async def do_delete_one(filter_dict: dict, collection: motor.motor_asyncio.AsyncIOMotorCollection) -> None:
    result = await collection.delete_one(filter_dict)
    logging.info('MongoDB delete one: filter {}'.format(filter_dict))
    return
