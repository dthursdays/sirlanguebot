from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

texts = {
    'analysis': {
        'ru': '📚 Словарь',
        'en-us': '📚 Dictionary',
        'en-gb': '📚 Dictionary',
        'es': '📚 Diccionario',
        'es-mx': '📚 Diccionario',
        'es-ar': '📚 Diccionario',
        'fr': '📚 Dictionnaire',
        'fr-ca': '📚 Dictionnaire',
        'de': '📚 Wörterbuch',
        'de-at': '📚 Wörterbuch',
        'de-ch': '📚 Wörterbuch',
        'it': '📚 Dizionario',
        'pt': '📚 Dicionário',
        'pt-br': '📚 Dicionário',
        'nl': '📚 Woordenboek'
    },
    'story': {
        'ru': '📝 Придумать историю',
        'en-us': '📝 Create a story',
        'en-gb': '📝 Create a story',
        'es': '📝 Crear una historia',
        'es-mx': '📝 Crear una historia',
        'es-ar': '📝 Crear una historia',
        'fr': '📝 Créer une histoire',
        'fr-ca': '📝 Créer une histoire',
        'de': '📝 Eine Geschichte erstellen',
        'de-at': '📝 Eine Geschichte erstellen',
        'de-ch': '📝 Eine Geschichte erstellen',
        'it': '📝 Creare una storia',
        'pt': '📝 Criar uma história',
        'pt-br': '📝 Criar uma história',
        'nl': '📝 Een verhaal maken'
    },
    'translate': {
        'ru': '💬 Перевод',
        'en-us': '💬 Translation',
        'en-gb': '💬 Translation',
        'es': '💬 Traducción',
        'es-mx': '💬 Traducción',
        'es-ar': '💬 Traducción',
        'fr': '💬 Traduction',
        'fr-ca': '💬 Traduction',
        'de': '💬 Übersetzung',
        'de-at': '💬 Übersetzung',
        'de-ch': '💬 Übersetzung',
        'it': '💬 Traduzione',
        'pt': '💬 Tradução',
        'pt-br': '💬 Tradução',
        'nl': '💬 Vertaling'
    },
    'settings': {
        'ru': '⚙️ Настройки',
        'en-us': '⚙️ Settings',
        'en-gb': '⚙️ Settings',
        'es': '⚙️ Configuración',
        'es-mx': '⚙️ Configuración',
        'es-ar': '⚙️ Configuración',
        'fr': '⚙️ Paramètres',
        'fr-ca': '⚙️ Paramètres',
        'de': '⚙️ Einstellungen',
        'de-at': '⚙️ Einstellungen',
        'de-ch': '⚙️ Einstellungen',
        'it': '⚙️ Impostazioni',
        'pt': '⚙️ Configurações',
        'pt-br': '⚙️ Configurações',
        'nl': '⚙️ Instellingen'
    },
    'back': {
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
    },
    'one_more': {
        'ru': '🔄 Еще',
        'en-us': '🔄 More',
        'en-gb': '🔄 More',
        'es': '🔄 Más',
        'es-mx': '🔄 Más',
        'es-ar': '🔄 Más',
        'fr': '🔄 Encore',
        'fr-ca': '🔄 Encore',
        'de': '🔄 Mehr',
        'de-at': '🔄 Mehr',
        'de-ch': '🔄 Mehr',
        'it': '🔄 Altro',
        'pt': '🔄 Mais',
        'pt-br': '🔄 Mais',
        'nl': '🔄 Meer'
    }
}


def ikb_menu(user):
    return InlineKeyboardMarkup(
        row_width=3,
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=texts['analysis'][user.native_language],
                    callback_data='analysis'),
            ],
            [
                InlineKeyboardButton(
                    text=texts['story'][user.native_language],
                    callback_data='story'),
            ],
            [
                InlineKeyboardButton(
                    text=texts['translate'][user.native_language],
                    callback_data='translate'),
            ],
            [
                InlineKeyboardButton(
                    text=texts['settings'][user.native_language],
                    callback_data='settings'),
            ],
        ]
        )


def ikb_back_to_menu(user):
    return InlineKeyboardMarkup(
        row_width=1,
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=texts['back'][user.native_language],
                    callback_data='main_menu'),
            ]
        ]
        )


def ikb_back_or_again(user):
    return InlineKeyboardMarkup(
        row_width=2,
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=texts['one_more'][user.native_language],
                    callback_data='story'),
            ],
            [
                InlineKeyboardButton(
                    text=texts['back'][user.native_language],
                    callback_data='main_menu'),
            ]
        ]
        )
