from aiogram import types

from data.messages.start_messages import Messages
from data.messages.story_messages import StoryMessages
from keyboards.inline import ikb_back_or_again, ikb_back_to_menu, ikb_menu
from loader import bot, dp
from utils.db_api import quick_commands as commands
from utils.edit_message import EditMessage
from utils.requests import story

edit_msg = EditMessage(bot)


@dp.callback_query_handler(lambda c: c.data == 'story')
async def tell_story(call: types.CallbackQuery):
    user_id = call.from_user.id
    user = await commands.select_user(user_id)

    if user.words == '':
        await edit_msg.edit_message(
            StoryMessages(user).come_back_later(),
            call,
            ikb_back_to_menu(user)
        )
        return

    await edit_msg.edit_message(
        StoryMessages(user).new_story(),
        call,
        None
    )

    language_to_learn = user.language_to_learn
    native_language = user.native_language

    try:
        text = await story(user.words, language_to_learn, native_language)
    except Exception as e:
        await bot.send_message(
            user_id,
            e + '\n' + StoryMessages(user).whats_next(),
            reply_markup=ikb_back_or_again(user)
        )
        return

    await bot.send_message(
        user_id,
        text,
        reply_markup=None
    )

    await bot.send_message(
        user_id,
        StoryMessages(user).whats_next(),
        reply_markup=ikb_back_or_again(user)
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
