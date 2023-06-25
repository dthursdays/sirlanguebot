from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from data.languages import languages
from data.messages.start_messages import Messages
from filters import HaveInDb, IsPrivate
from keyboards.inline import get_ikb_languages, ikb_menu
from loader import bot, dp
from states.regist import Regist
from utils.db_api import quick_commands as commands
from utils.edit_message import EditMessage

edit_msg = EditMessage(bot)


@dp.message_handler(Command("start", prefixes="/"), IsPrivate())
async def command_start(message: types.Message):
    user_id = message.from_user.id
    user = await commands.select_user(user_id)

    if user is None:
        await message.answer(
            Messages.language_native_mes(message),
            reply_markup=get_ikb_languages()
        )
        await Regist.native_language.set()
        return

    if user.status == 'active':
        text = Messages(user).finish_registration()
        markup = ikb_menu(user)
    elif user.status == 'baned':
        text = 'Ты забанен!'
        markup = None

    await message.answer(
        text,
        parse_mode='HTML',
        reply_markup=markup
    )


@dp.callback_query_handler(HaveInDb(False),
                           lambda c: c.data in [
                               language for language in languages
                               ],
                           state=Regist.native_language)
async def set_native(call: types.CallbackQuery, state: FSMContext):
    native_language = call.data
    user_id = call.from_user.id
    first_name = call.from_user.first_name
    last_name = call.from_user.last_name
    username = call.from_user.username

    try:
        await commands.add_user(user_id=user_id,
                                first_name=first_name,
                                last_name=last_name,
                                username=username,
                                status='active',
                                native_language=native_language,
                                language_to_learn='',
                                words='')
    except Exception as e:
        raise e

    await state.finish()

    user = await commands.select_user(user_id)
    await edit_msg.edit_message(
        Messages(user).language_to_learn_mes(),
        call,
        get_ikb_languages(user)
    )
    await Regist.language_to_learn.set()


@dp.callback_query_handler(lambda c: c.data in [
                               language for language in languages
                               ],
                           state=Regist.language_to_learn)
async def set_to_learn(call: types.CallbackQuery, state: FSMContext):
    language_to_learn = call.data
    user_id = call.from_user.id

    try:
        await commands.update_to_learn(user_id,
                                       language_to_learn=language_to_learn)
    except Exception as e:
        raise e

    user = await commands.select_user(user_id)
    await edit_msg.edit_message(
        Messages(user).finish_registration(),
        call,
        ikb_menu(user)
    )
    await state.finish()


@dp.message_handler(IsPrivate(), text='/ban')
async def get_ban(message: types.Message):
    user = await commands.select_user(message.from_user.id)
    await commands.update_status(user, 'ban')
    await message.answer('Ты забанен!')


@dp.message_handler(IsPrivate(), text='/unban')
async def remove_ban(message: types.Message):
    user = await commands.select_user(message.from_user.id)
    await commands.update_status(user, 'active')
    await message.answer('Тебя разбанили!')
