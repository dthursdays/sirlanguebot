from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data.languages import languages


class SettingsButtons:
    def __init__(self, user):
        self.user = user

    def update_native(self):
        native_emoji = languages.get(self.user.native_language)[:2]
        text = {
            'ru': f'{native_emoji} Изменить язык',
            'en-us': f'{native_emoji} Change language',
            'en-gb': f'{native_emoji} Change language',
            'es': f'{native_emoji} Cambiar idioma',
            'es-mx': f'{native_emoji} Cambiar idioma',
            'es-ar': f'{native_emoji} Cambiar idioma',
            'fr': f'{native_emoji} Changer de langue',
            'fr-ca': f'{native_emoji} Changer de langue',
            'de': f'{native_emoji} Sprache ändern',
            'de-at': f'{native_emoji} Sprache ändern',
            'de-ch': f'{native_emoji} Sprache ändern',
            'it': f'{native_emoji} Cambia lingua',
            'pt': f'{native_emoji} Alterar idioma',
            'pt-br': f'{native_emoji} Alterar idioma',
            'nl': f'{native_emoji} Taal wijzigen'
        }
        return text[self.user.native_language]

    def update_to_learn(self):
        to_learn_emoji = languages.get(self.user.language_to_learn)[:2]
        text = {
            'ru': f'{to_learn_emoji} Изменить язык для изучения',
            'en-us': f'{to_learn_emoji} Change language for learning',
            'en-gb': f'{to_learn_emoji} Change language for learning',
            'es': f'{to_learn_emoji} Cambiar idioma para el aprendizaje',
            'es-mx': f'{to_learn_emoji} Cambiar idioma para el aprendizaje',
            'es-ar': f'{to_learn_emoji} Cambiar idioma para el aprendizaje',
            'fr': f'{to_learn_emoji} Changer de langue pour l\'apprentissage',
            'fr-ca': f'{to_learn_emoji} Changer de langue pour l\'apprentissage',
            'de': f'{to_learn_emoji} Sprache für das Lernen ändern',
            'de-at': f'{to_learn_emoji} Sprache für das Lernen ändern',
            'de-ch': f'{to_learn_emoji} Sprache für das Lernen ändern',
            'it': f'{to_learn_emoji} Cambia lingua per l\'apprendimento',
            'pt': f'{to_learn_emoji} Alterar idioma para aprendizado',
            'pt-br': f'{to_learn_emoji} Alterar idioma para aprendizado',
            'nl': f'{to_learn_emoji} Taal wijzigen voor leren'
        }
        return text[self.user.native_language]

    def clear_words(self):
        text = {
            'ru': '🧹 Очистить память',
            'en-us': '🧹 Clear Memory',
            'en-gb': '🧹 Clear Memory',
            'es': '🧹 Limpiar Memoria',
            'es-mx': '🧹 Limpiar Memoria',
            'es-ar': '🧹 Limpiar Memoria',
            'fr': '🧹 Effacer la Mémoire',
            'fr-ca': '🧹 Effacer la Mémoire',
            'de': '🧹 Speicher Löschen',
            'de-at': '🧹 Speicher Löschen',
            'de-ch': '🧹 Speicher Löschen',
            'it': '🧹 Pulisci la Memoria',
            'pt': '🧹 Limpar Memória',
            'pt-br': '🧹 Limpar Memória',
            'nl': '🧹 Geheugen Wissen'
        }
        return text[self.user.native_language]

    def back(self):
        text = {
            'ru': '🔙 Назад',
            'en-us': '🔙 Back',
            'en-gb': '🔙 Back',
            'es': '🔙 Volver',
            'es-mx': '🔙 Regresar',
            'es-ar': '🔙 Volver',
            'fr': '🔙 Retour',
            'fr-ca': '🔙 Retour',
            'de': '🔙 Zurück',
            'de-at': '🔙 Zurück',
            'de-ch': '🔙 Zurück',
            'it': '🔙 Indietro',
            'pt': '🔙 Voltar',
            'pt-br': '🔙 Voltar',
            'nl': '🔙 Terug'
        }
        return text[self.user.native_language]


def ikb_settings(user):
    return InlineKeyboardMarkup(
        row_width=1,
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=SettingsButtons(user).update_native(),
                    callback_data='update_native'),
            ],
            [
                InlineKeyboardButton(
                    text=SettingsButtons(user).update_to_learn(),
                    callback_data='update_to_learn'),
            ],
            [
                InlineKeyboardButton(
                    text=SettingsButtons(user).clear_words(),
                    callback_data='clear_words'),
            ],
            [
                InlineKeyboardButton(
                    text=SettingsButtons(user).back(),
                    callback_data='main_menu'),
            ]
        ]
        )
