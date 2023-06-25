from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from data.languages import languages
from utils.db_api import quick_commands as commands

# class IsAdmin(BoundFilter):
#     key = "is_admin"
#
#     def __init__(self, admin):
#         self.admin = admin
#
#     async def check(self, msg: Message):


class HaveInDb(BoundFilter):
    def __init__(self, consist):
        self.consist = consist

    async def check(self, call: types.CallbackQuery):
        if await commands.select_user(call.from_user.id):
            return self.consist
        if call.data not in [language for language in languages]:
            await call.answer(
                'You are not registered yet!\nUse /start to register.'
            )
        return not self.consist
