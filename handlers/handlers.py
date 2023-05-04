import json
import torch
import transformers
import logging

from db.mongo import users, do_find_one, do_insert_one, do_find_many, do_delete_one
from transformers import AutoModelForCausalLM, AutoTokenizer


tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium", padding_side='left')
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")
logging.basicConfig(level=logging.DEBUG)


async def start_bot(data: dict):
    return "Hello! I'm a simple GPT2 chat bot which was designed as a homework project for 'NLP and ChatBots course'" \
           " at Synergy University. I understand only English words and store some dialogue history. Ask me something."


async def answer(data: dict):
    if data['message']['text'] is not None:
        input_ids = tokenizer.encode(data['message']['text'] + tokenizer.eos_token, return_tensors='pt')
        chat_ids = model.generate(input_ids, max_length=500, pad_token_id=tokenizer.eos_token_id)
        response = tokenizer.decode(chat_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    else:
        response = 'I do not understand you...'
    return response


async def message_handle(data: dict) -> dict:
    logging.warning("message_handle: {}".format(data['message']))
    if 'text' in data['message'].keys():
        command = data['message']['text']
        message = {
            'chat_id': data['message']['chat']['id'],
            'text': None
        }

        # /start
        if command == '/start':
            message['text'] = await start_bot(data)
        else:
            message['text'] = await answer(data)
    else:
        message = 'I do not understand you...'

    return message
