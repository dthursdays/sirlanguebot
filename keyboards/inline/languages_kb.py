from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data.languages import languages


def get_ikb_languages(user=None):
    ikb_languages = InlineKeyboardMarkup(row_width=2)

    if not user:
        for language in languages:
            ikb_languages.insert(
                InlineKeyboardButton(
                    text=languages.get(language),
                    callback_data=language
                    )
                )
        return ikb_languages

    for language in languages:
        if (
            language != user.language_to_learn and
            language != user.native_language
        ):
            ikb_languages.insert(
                InlineKeyboardButton(
                    text=languages.get(language),
                    callback_data=language
                    )
                )
    return ikb_languages
