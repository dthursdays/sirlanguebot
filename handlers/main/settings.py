import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext

from data.languages import languages
from data.messages.settings_messages import SettingsMessages
from data.messages.start_messages import Messages
from keyboards.inline import get_ikb_languages, ikb_menu, ikb_settings
from loader import bot, dp
from states.regist import Regist
from utils.db_api import quick_commands as commands
from utils.edit_message import EditMessage

edit_msg = EditMessage(bot)


@dp.callback_query_handler(lambda c: c.data == 'settings')
async def settings_menu(call: types.CallbackQuery):
    user_id = call.from_user.id
    user = await commands.select_user(user_id)

    await edit_msg.edit_message(
        SettingsMessages(user).settings(),
        call,
        ikb_settings(user)
        )


@dp.callback_query_handler(lambda c: c.data == 'update_native')
async def settings_native(call: types.CallbackQuery):
    user_id = call.from_user.id
    user = await commands.select_user(user_id)
    await edit_msg.edit_message(
        SettingsMessages(user).update_native(),
        call,
        get_ikb_languages(user)
    )
    await Regist.update_native.set()


@dp.callback_query_handler(lambda c: c.data in [
                               language for language in languages
                               ],
                           state=Regist.update_native)
async def update_native(call: types.CallbackQuery, state: FSMContext):
    native_language = call.data
    user_id = call.from_user.id

    try:
        await commands.update_native(
            user_id,
            native_language=native_language
            )
    except Exception as e:
        raise e

    user = await commands.select_user(user_id)
    await edit_msg.edit_message(
        SettingsMessages(user).language_updated(),
        call,
        None
    )
    await state.finish()

    await asyncio.sleep(3)
    await edit_msg.edit_message(
        SettingsMessages(user).settings(),
        call,
        ikb_settings(user)
        )


@dp.callback_query_handler(lambda c: c.data == 'update_to_learn')
async def settings_to_learn(call: types.CallbackQuery):
    user_id = call.from_user.id
    user = await commands.select_user(user_id)
    await edit_msg.edit_message(
        SettingsMessages(user).update_to_learn(),
        call,
        get_ikb_languages(user)
    )
    await Regist.update_to_learn.set()


@dp.callback_query_handler(lambda c: c.data in [
                               language for language in languages
                               ],
                           state=Regist.update_to_learn)
async def update_to_learn(call: types.CallbackQuery, state: FSMContext):
    language_to_learn = call.data
    user_id = call.from_user.id

    try:
        await commands.update_to_learn(
            user_id,
            language_to_learn=language_to_learn
            )
    except Exception as e:
        raise e

    user = await commands.select_user(user_id)
    await edit_msg.edit_message(
        SettingsMessages(user).language_updated(),
        call,
        None
    )
    await state.finish()

    await asyncio.sleep(3)
    await edit_msg.edit_message(
        SettingsMessages(user).settings(),
        call,
        ikb_settings(user)
        )


@dp.callback_query_handler(lambda c: c.data == 'clear_words')
async def clear_words(call: types.CallbackQuery):
    user = await commands.select_user(call.from_user.id)
    await user.update(words='').apply()

    await edit_msg.edit_message(
        SettingsMessages(user).words_clear(),
        call,
        None
    )
    await asyncio.sleep(3)
    await edit_msg.edit_message(
        SettingsMessages(user).settings(),
        call,
        ikb_settings(user)
        )


@dp.callback_query_handler(lambda c: c.data == 'main_menu')
async def back_to_menu(call: types.CallbackQuery):
    user_id = call.from_user.id
    user = await commands.select_user(user_id)
    await edit_msg.edit_message(
            Messages(user).finish_registration(),
            call,
            ikb_menu(user)
        )
    return
