from aiogram import types


class EditMessage:
    def __init__(self, bot):
        self.bot = bot

    async def edit_message(self, new_text, aio_type,
                           ikb=None, chat_id=None, parse_mode='HTML'):

        if isinstance(aio_type, types.CallbackQuery):
            message_id = aio_type.message.message_id
            chat_id = aio_type.from_user.id
        elif isinstance(aio_type, types.Message):
            if chat_id is None:
                raise Exception('Изменяется Message, но не указан chat_id')
            message_id = aio_type.message_id

        if new_text is not None:
            await self.bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text=new_text,
                parse_mode=parse_mode
                )
        if ikb is not None:
            await self.bot.edit_message_reply_markup(
                chat_id=chat_id,
                message_id=message_id,
                reply_markup=ikb
                )
