from aiogram.dispatcher.filters.state import State, StatesGroup


class Regist(StatesGroup):
    native_language = State()
    language_to_learn = State()

    msg = State()

    phrase_translation = State()
    word_analysis = State()

    update_native = State()
    update_to_learn = State()
