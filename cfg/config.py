from os import environ

MONGO_URL = environ.get("MONGO_URL")
RABBITMQ_URL = environ.get("RABBITMQ_URL")

TELEGRAM_TOKEN = environ.get("TELEGRAM_TOKEN")
TELEGRAM_WEBHOOK = environ.get("TELEGRAM_WEBHOOK")

ADMIN_CHAT_ID = environ.get("TELEGRAM_ADMIN_CHAT_ID")

ADMIN_MODE = True
