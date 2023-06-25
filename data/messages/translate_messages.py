import aiogram.utils.markdown as fmt


class TranslateMessages:
    def __init__(self, user):
        self.user = user

    def type_a_phrase(self):
        messages = {
            'ru': 'Введите текст:',
            'en-us': 'Enter text:',
            'en-gb': 'Enter text:',
            'es': 'Ingrese texto:',
            'es-mx': 'Ingrese texto:',
            'es-ar': 'Ingrese texto:',
            'fr': 'Entrez le texte :',
            'fr-ca': 'Entrez le texte :',
            'de': 'Text eingeben:',
            'de-at': 'Text eingeben:',
            'de-ch': 'Text eingeben:',
            'it': 'Inserisci il testo:',
            'pt': 'Insira o texto:',
            'pt-br': 'Insira o texto:',
            'nl': 'Voer tekst in:'
        }

        return fmt.text(fmt.hbold(messages[self.user.native_language]))

    def thinking(self):
        messages = {
            'ru': 'Думаю...',
            'en-us': 'I think...',
            'en-gb': 'I think...',
            'es': 'Creo...',
            'es-mx': 'Creo...',
            'es-ar': 'Creo...',
            'fr': 'Je pense...',
            'fr-ca': 'Je pense...',
            'de': 'Ich denke...',
            'de-at': 'Ich denke...',
            'de-ch': 'Ich denke...',
            'it': 'Penso...',
            'pt': 'Eu acho...',
            'pt-br': 'Eu acho...',
            'nl': 'Ik denk...'
        }

        return fmt.text(fmt.hbold(messages[self.user.native_language]))
