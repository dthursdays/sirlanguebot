import aiogram.utils.markdown as fmt


class StoryMessages:
    def __init__(self, user):
        self.user = user

    def come_back_later(self):
        messages = {
            'ru': 'Возвращайся, когда воспользуешься словарем или переводом',
            'en-us': 'Come back when you use the dictionary or translation',
            'en-gb': 'Come back when you use the dictionary or translation',
            'es': 'Vuelve cuando uses el diccionario o la traducción',
            'es-mx': 'Vuelve cuando uses el diccionario o la traducción',
            'es-ar': 'Vuelve cuando uses el diccionario o la traducción',
            'fr': 'Reviens quand tu utiliseras le dictionnaire ou la traduction',
            'fr-ca': 'Reviens quand tu utiliseras le dictionnaire ou la traduction',
            'de': 'Komm zurück, wenn du das Wörterbuch oder die Übersetzung benutzt',
            'de-at': 'Komm zurück, wenn du das Wörterbuch oder die Übersetzung benutzt',
            'de-ch': 'Komm zurück, wenn du das Wörterbuch oder die Übersetzung benutzt',
            'it': 'Torna quando usi il dizionario o la traduzione:',
            'pt': 'Volte quando usar o dicionário ou a tradução:',
            'pt-br': 'Volte quando usar o dicionário ou a tradução:',
            'nl': 'Kom terug als je het woordenboek of de vertaling gebruikt:'
        }
        return fmt.text(fmt.hbold(messages[self.user.native_language]))

    def new_story(self):
        messages = {
            'ru': 'Сочиняю историю...',
            'en-us': 'Crafting a story...',
            'en-gb': 'Creating a story...',
            'es': 'Creando una historia...',
            'es-mx': 'Elaborando una historia...',
            'es-ar': 'Creando una historia...',
            'fr': 'En train de composer une histoire...',
            'fr-ca': 'En train de créer une histoire...',
            'de': 'Eine Geschichte verfassen...',
            'de-at': 'Eine Geschichte schreiben...',
            'de-ch': 'Eine Geschichte verfassen...',
            'it': 'Sto creando una storia...',
            'pt': 'Criando uma história...',
            'pt-br': 'Elaborando uma história...',
            'nl': 'Een verhaal aan het schrijven...'
        }
        return fmt.text(fmt.hbold(messages[self.user.native_language]))

    def whats_next(self):
        messages = {
            'ru': 'Что дальше?',
            'en-us': 'What\'s next?',
            'en-gb': 'What\'s next?',
            'es': '¿Qué sigue?',
            'es-mx': '¿Qué sigue?',
            'es-ar': '¿Qué sigue?',
            'fr': 'Qu\'est-ce qui vient ensuite?',
            'fr-ca': 'Qu\'est-ce qui vient ensuite?',
            'de': 'Was kommt als nächstes?',
            'de-at': 'Was kommt als nächstes?',
            'de-ch': 'Was kommt als nächstes?',
            'it': 'Cosa succede dopo?',
            'pt': 'O que vem a seguir?',
            'pt-br': 'O que vem a seguir?',
            'nl': 'Wat komt hierna?'
        }
        return fmt.text(fmt.hbold(messages[self.user.native_language]))
