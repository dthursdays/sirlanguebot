from aiogram import types
from aiogram.dispatcher import FSMContext

from data.messages.analysis_messages import AnalysisMessages
from data.messages.start_messages import Messages
from filters import HaveInDb
from keyboards.inline import ikb_back_to_menu, ikb_menu
from loader import bot, dp
from states.regist import Regist
from utils.db_api import quick_commands as commands
from utils.edit_message import EditMessage
from utils.requests import analysis

edit_msg = EditMessage(bot)


@dp.callback_query_handler(HaveInDb(True), lambda c: c.data == 'analysis')
async def word_analysis(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    user = await commands.select_user(user_id)

    async with state.proxy() as data:
        data['last'] = call

    await edit_msg.edit_message(
            AnalysisMessages(user).type_a_word(),
            call,
            ikb_back_to_menu(user)
        )
    await Regist.word_analysis.set()


@dp.message_handler(state=Regist.word_analysis)
async def get_analysis(message: types.Message, state: FSMContext):
    words = message.text
    user_id = message.from_user.id
    user = await commands.select_user(user_id)
    language_to_learn = user.language_to_learn
    native_language = user.native_language
    word_list = words.split()
    word = word_list[0]

    async with state.proxy() as data:
        last = data['last']
    await edit_msg.edit_message(
            None,
            last,
            '',
            user_id
        )

    await commands.update_words(user_id, word)

    if len(word_list) > 1:
        msg = await message.answer(
            AnalysisMessages(user).more_than_one()
        )
    else:
        msg = await message.answer(
            AnalysisMessages(user).thinking()
        )

    try:
        text = await analysis(word, language_to_learn, native_language)
    except Exception as e:
        msg = await bot.send_message(
            user_id,
            e + '\n' + AnalysisMessages(user).type_a_word(),
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
            AnalysisMessages(user).type_a_word(),
            reply_markup=ikb_back_to_menu(user)
        )

    async with state.proxy() as data:
        data['last'] = msg


@dp.callback_query_handler(lambda c: c.data == 'main_menu',
                           state=Regist.word_analysis)
async def back_to_menu(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    user = await commands.select_user(user_id)

    await edit_msg.edit_message(
            Messages(user).finish_registration(),
            call,
            ikb_menu(user)
        )
    await state.finish()
