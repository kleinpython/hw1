import logging
from aiogram.utils import executor
from config import dp
from handlers import client, callback, admin, extra

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
callback.register_handlers_callback(dp)

extra.register_handlers_extra(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
