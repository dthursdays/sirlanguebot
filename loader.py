import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from data import config
from utils.db_api.db_gino import db

debug = config.DEBUG
logging.basicConfig(
    format=u'%(filename)s [LINE:%(lineno)d] '
           u'#%(levelname)-8s [%(asctime)s]  %(message)s',
    filename="py_log.log",
    level=debug
    )

bot = Bot(token=config.API_TOKEN, parse_mode=types.ParseMode.HTML)

storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)

dp.middleware.setup(LoggingMiddleware())


# edit_ls = EditLastMessage(bot)


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


__all__ = ['bot', 'db', 'storage', 'dp']
