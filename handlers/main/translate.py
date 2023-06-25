from aiogram import types
from aiogram.dispatcher import FSMContext

from data.messages.start_messages import Messages
from data.messages.translate_messages import TranslateMessages
from keyboards.inline import ikb_back_to_menu, ikb_menu
from loader import bot, dp
from states.regist import Regist
from utils.db_api import quick_commands as commands
from utils.edit_message import EditMessage
from utils.requests import translate

edit_msg = EditMessage(bot)


@dp.callback_query_handler(lambda c: c.data == 'translate')
async def phrase_translate(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    user = await commands.select_user(user_id)

    async with state.proxy() as data:
        data['last'] = call

    await edit_msg.edit_message(
            TranslateMessages(user).type_a_phrase(),
            call,
            ikb_back_to_menu(user)
        )
    await Regist.phrase_translation.set()
    return


@dp.message_handler(state=Regist.phrase_translation)
async def get_translate(message: types.Message, state: FSMContext):
    words = message.text
    user_id = message.from_user.id
    user = await commands.select_user(user_id)
    language_to_learn = user.language_to_learn
    native_language = user.native_language

    async with state.proxy() as data:
        last = data['last']
    await edit_msg.edit_message(
            None,
            last,
            '',
            user_id
        )

    await commands.update_words(user_id, words)

    msg = await message.answer(
            TranslateMessages(user).thinking()
        )
    try:
        text = await translate(words, language_to_learn, native_language)
    except Exception as e:
        msg = await bot.send_message(
            user_id,
            e + '\n' + TranslateMessages(user).type_a_phrase(),
            reply_markup=ikb_back_to_menu(user)
        )
        async with state.proxy() as data:
            data['last'] = msg
        return

    await edit_msg.edit_message(
            text,
            msg,
            chat_id=user_id
        )

    msg = await bot.send_message(
            user_id,
            TranslateMessages(user).type_a_phrase(),
            reply_markup=ikb_back_to_menu(user)
        )

    async with state.proxy() as data:
        data['last'] = msg


@dp.callback_query_handler(lambda c: c.data == 'main_menu',
                           state=Regist.phrase_translation)
async def back_to_menu(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    user = await commands.select_user(user_id)

    await edit_msg.edit_message(
            Messages(user).finish_registration(),
            call,
            ikb_menu(user)
        )
    await state.finish()
    return
