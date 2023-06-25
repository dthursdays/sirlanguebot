import aiogram.utils.markdown as fmt


class Messages:
    def __init__(self, user):
        self.user = user

    @staticmethod
    def language_native_mes(aio_type):
        return fmt.text(
            f'✌️ Hi, {aio_type.from_user.first_name}.\n',
            fmt.hbold('🌐 Choose your native language: ')
        )

    def language_to_learn_mes(self):
        text = {
            'ru': '🌐 Выберите язык для изучения:',
            'en-us': '🌐 Choose a language to learn:',
            'en-gb': '🌐 Choose a language to learn:',
            'es': '🌐 Elige un idioma para aprender:',
            'es-mx': '🌐 Elige un idioma para aprender:',
            'es-ar': '🌐 Elige un idioma para aprender:',
            'fr': '🌐 Choisissez une langue à apprendre:',
            'fr-ca': '🌐 Choisissez une langue à apprendre:',
            'de': '🌐 Wähle eine Sprache zum Lernen:',
            'de-at': '🌐 Wähle eine Sprache zum Lernen:',
            'de-ch': '🌐 Wähle eine Sprache zum Lernen:',
            'it': '🌐 Scegli una lingua da imparare:',
            'pt': '🌐 Escolha um idioma para aprender:',
            'pt-br': '🌐 Escolha um idioma para aprender:',
            'nl': '🌐 Kies een taal om te leren:'
        }
        return fmt.text(fmt.hbold(text[self.user.native_language]))

    def finish_registration(self):
        text = {
            'ru': 'Я могу найти слово в словаре и переводить тексты. Также я запоминаю все слова и могу сочинять из них истории.',
            'en-us': 'I can look up words in the dictionary and translate texts. I also remember all the words and can compose stories from them.',
            'en-gb': 'I can look up words in the dictionary and translate texts. I also remember all the words and can compose stories from them.',
            'es': 'Puedo buscar palabras en el diccionario y traducir textos. También recuerdo todas las palabras y puedo componer historias con ellas.',
            'es-mx': 'Puedo buscar palabras en el diccionario y traducir textos. También recuerdo todas las palabras y puedo componer historias con ellas.',
            'es-ar': 'Puedo buscar palabras en el diccionario y traducir textos. También recuerdo todas las palabras y puedo componer historias con ellas.',
            'fr': 'Je peux rechercher des mots dans le dictionnaire et traduire des textes. Je me souviens également de tous les mots et je peux composer des histoires avec eux.',
            'fr-ca': 'Je peux rechercher des mots dans le dictionnaire et traduire des textes. Je me souviens également de tous les mots et je peux composer des histoires avec eux.',
            'de': 'Ich kann Wörter im Wörterbuch nachschlagen und Texte übersetzen. Ich erinnere mich auch an alle Wörter und kann Geschichten daraus verfassen.',
            'de-at': 'Ich kann Wörter im Wörterbuch nachschlagen und Texte übersetzen. Ich erinnere mich auch an alle Wörter und kann Geschichten daraus verfassen.',
            'de-ch': 'Ich kann Wörter im Wörterbuch nachschlagen und Texte übersetzen. Ich erinnere mich auch an alle Wörter und kann Geschichten daraus verfassen.',
            'it': 'Posso cercare le parole nel dizionario e tradurre i testi. Ricordo anche tutte le parole e posso comporre storie con esse.',
            'pt': 'Posso procurar palavras no dicionário e traduzir textos. Também me lembro de todas as palavras e posso compor histórias com elas.',
            'pt-br': 'Posso procurar palavras no dicionário e traduzir textos. Também me lembro de todas as palavras e posso compor histórias com elas.',
            'nl': 'Ik kan woorden opzoeken in het woordenboek en teksten vertalen. Ik herinner me ook alle woorden en kan er verhalen van maken.'
        }
        return fmt.text(fmt.hbold(text[self.user.native_language]))
