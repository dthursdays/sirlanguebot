import aiogram.utils.markdown as fmt

from data.languages import languages


class SettingsMessages:
    def __init__(self, user):
        self.user = user

    def settings(self):
        text = {
            'ru': 'ㅤㅤㅤㅤ⚙️ Настройкиㅤㅤ',
            'en-us': 'ㅤㅤㅤㅤ⚙️ Settingsㅤㅤ',
            'en-gb': 'ㅤㅤㅤㅤ⚙️ Settingsㅤㅤ',
            'es': 'ㅤㅤㅤㅤ⚙️ Configuraciónㅤㅤ',
            'es-mx': 'ㅤㅤㅤㅤ⚙️ Configuraciónㅤㅤ',
            'es-ar': 'ㅤㅤㅤㅤ⚙️ Configuraciónㅤㅤ',
            'fr': 'ㅤㅤㅤㅤ⚙️ Paramètresㅤㅤ',
            'fr-ca': 'ㅤㅤㅤㅤ⚙️ Paramètresㅤㅤ',
            'de': 'ㅤㅤㅤㅤ⚙️ Einstellungenㅤㅤ',
            'de-at': 'ㅤㅤㅤㅤ⚙️ Einstellungenㅤㅤ',
            'de-ch': 'ㅤㅤㅤㅤ⚙️ Einstellungenㅤㅤ',
            'it': 'ㅤㅤㅤㅤ⚙️ Impostazioniㅤㅤ',
            'pt': 'ㅤㅤㅤㅤ⚙️ Configuraçõesㅤㅤ',
            'pt-br': 'ㅤㅤㅤㅤ⚙️ Configuraçõesㅤㅤ',
            'nl': 'ㅤㅤㅤㅤ⚙️ Instellingenㅤㅤ'
        }
        return fmt.text(fmt.hbold(text[self.user.native_language]))

    def update_native(self):
        text = {
            'ru': '🇷🇺 Русский\nВыберите новый язык:',
            'en-us': '🇺🇸 American English\nChoose a new language:',
            'en-gb': '🇬🇧 British English\nChoose a new language:',
            'es': '🇪🇸 Español\nElija un nuevo idioma:',
            'es-mx': '🇲🇽 Español (México)\nElija un nuevo idioma:',
            'es-ar': '🇦🇷 Español (Argentina)\nElija un nuevo idioma:',
            'fr': '🇫🇷 Français\nChoisissez une nouvelle langue:',
            'fr-ca': '🇨🇦 Français (Canada)\nChoisissez une nouvelle langue:',
            'de': '🇩🇪 Deutsch\nWählen Sie eine neue Sprache:',
            'de-at': '🇦🇹 Deutsch (Österreich)\nWählen Sie eine neue Sprache:',
            'de-ch': '🇨🇭 Deutsch (Schweiz)\nWählen Sie eine neue Sprache:',
            'it': '🇮🇹 Italiano\nScegli una nuova lingua:',
            'pt': '🇵🇹 Português\nEscolha um novo idioma:',
            'pt-br': '🇧🇷 Português (Brasil)\nEscolha um novo idioma:',
            'nl': '🇳🇱 Nederlands\nKies een nieuwe taal:'
        }
        return fmt.text(fmt.hbold(text[self.user.native_language]))

    def update_to_learn(self):
        to_learn = languages.get(self.user.language_to_learn)
        text = {
            'ru': f'{to_learn}\nВыберите новый язык для изучения:',
            'en-us': f'{to_learn}\nChoose a new language to learn:',
            'en-gb': f'{to_learn}\nChoose a new language to learn:',
            'es': f'{to_learn}\nElige un nuevo idioma para aprender:',
            'es-mx': f'{to_learn}\nElige un nuevo idioma para aprender:',
            'es-ar': f'{to_learn}\nElige un nuevo idioma para aprender:',
            'fr': f'{to_learn}\nChoisissez une nouvelle langue à apprendre:',
            'fr-ca': f'{to_learn}\nChoisissez une nouvelle langue à apprendre:',
            'de': f'{to_learn}\nWählen Sie eine neue Sprache zum Lernen:',
            'de-at': f'{to_learn}\nWählen Sie eine neue Sprache zum Lernen:',
            'de-ch': f'{to_learn}\nWählen Sie eine neue Sprache zum Lernen:',
            'it': f'{to_learn}\nScegli una nuova lingua da imparare:',
            'pt': f'{to_learn}\nEscolha um novo idioma para aprender:',
            'pt-br': f'{to_learn}\nEscolha um novo idioma para aprender:',
            'nl': f'{to_learn}\nKies een nieuwe taal om te leren:'
        }
        return fmt.text(fmt.hbold(text[self.user.native_language]))

    def language_updated(self):
        text = {
            'ru': '🔄 Язык успешно изменен',
            'en-us': '🔄 Language successfully changed',
            'en-gb': '🔄 Language successfully changed',
            'es': '🔄 Idioma cambiado correctamente',
            'es-mx': '🔄 Idioma cambiado correctamente',
            'es-ar': '🔄 Idioma cambiado correctamente',
            'fr': '🔄 Langue modifiée avec succès',
            'fr-ca': '🔄 Langue modifiée avec succès',
            'de': '🔄 Sprache erfolgreich geändert',
            'de-at': '🔄 Sprache erfolgreich geändert',
            'de-ch': '🔄 Sprache erfolgreich geändert',
            'it': '🔄 Lingua modificata con successo',
            'pt': '🔄 Idioma alterado com sucesso',
            'pt-br': '🔄 Idioma alterado com sucesso',
            'nl': '🔄 Taal succesvol gewijzigd'
        }
        return fmt.text(fmt.hbold(text[self.user.native_language]))

    def words_clear(self):
        text = {
            'ru': '💭 Я больше не помню ни единого твоего слова',
            'en-us': '💭 I don\'t remember a single word you said',
            'en-gb': '💭 I don\'t remember a single word you said',
            'es': '💭 No recuerdo ni una sola palabra que dijiste',
            'es-mx': '💭 No recuerdo ni una sola palabra que dijiste',
            'es-ar': '💭 No recuerdo ni una sola palabra que dijiste',
            'fr': '💭 Je ne me souviens plus d\'un seul mot que tu as dit',
            'fr-ca': '💭 Je ne me souviens plus d\'un seul mot que tu as dit',
            'de': '💭 Ich erinnere mich nicht an ein einziges Wort, das du gesagt hast',
            'de-at': '💭 Ich erinnere mich nicht an ein einziges Wort, das du gesagt hast',
            'de-ch': '💭 Ich erinnere mich nicht an ein einziges Wort, das du gesagt hast',
            'it': '💭 Non ricordo una sola parola che hai detto',
            'pt': '💭 Não me lembro de uma única palavra que você disse',
            'pt-br': '💭 Não me lembro de uma única palavra que você disse',
            'nl': '💭 Ik herinner me geen enkel woord dat je hebt gezegd'
        }
        return fmt.text(fmt.hbold(text[self.user.native_language]))
