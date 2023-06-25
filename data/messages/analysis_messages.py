import aiogram.utils.markdown as fmt


class AnalysisMessages:
    def __init__(self, user):
        self.user = user

    def type_a_word(self):
        messages = {
            'ru': 'Введите слово:',
            'en-us': 'Enter a word:',
            'en-gb': 'Enter a word:',
            'es': 'Ingrese una palabra:',
            'es-mx': 'Ingrese una palabra:',
            'es-ar': 'Ingrese una palabra:',
            'fr': 'Entrez un mot :',
            'fr-ca': 'Entrez un mot :',
            'de': 'Geben Sie ein Wort ein:',
            'de-at': 'Geben Sie ein Wort ein:',
            'de-ch': 'Geben Sie ein Wort ein:',
            'it': 'Inserisci una parola:',
            'pt': 'Digite uma palavra:',
            'pt-br': 'Digite uma palavra:',
            'nl': 'Voer een woord in:',
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

    def more_than_one(self):
        messages = {
            'ru': 'Я могу обработать только одно слово за раз, потому возьму первое из указанных.\nДумаю...',
            'en-us': 'I can process only one word at a time, so I will take the first one from the given.\nI think...',
            'en-gb': 'I can process only one word at a time, so I will take the first one from the given.\nI think...',
            'es': 'Puedo procesar solo una palabra a la vez, así que tomaré la primera de las indicadas.\nCreo que...',
            'es-mx': 'Puedo procesar solo una palabra a la vez, así que tomaré la primera de las indicadas.\nCreo que...',
            'es-ar': 'Puedo procesar solo una palabra a la vez, así que tomaré la primera de las indicadas.\nCreo que...',
            'fr': 'Je ne peux traiter qu\'un mot à la fois, donc je prendrai le premier de ceux indiqués.\nJe pense...',
            'fr-ca': 'Je ne peux traiter qu\'un mot à la fois, donc je prendrai le premier de ceux indiqués.\nJe pense...',
            'de': 'Ich kann nur ein Wort auf einmal verarbeiten, also nehme ich das erste aus der Liste.\nIch denke...',
            'de-at': 'Ich kann nur ein Wort auf einmal verarbeiten, also nehme ich das erste aus der Liste.\nIch denke...',
            'de-ch': 'Ich kann nur ein Wort auf einmal verarbeiten, also nehme ich das erste aus der Liste.\nIch denke...',
            'it': 'Posso elaborare solo una parola alla volta, quindi prenderò la prima tra quelle indicate.\nPenso che...',
            'pt': 'Eu só posso processar uma palavra de cada vez, então vou pegar a primeira da lista.\nEu acho que...',
            'pt-br': 'Eu só posso processar uma palavra de cada vez, então vou pegar a primeira da lista.\nEu acho que...',
            'nl': 'Ik kan slechts één woord per keer verwerken, dus ik neem het eerste woord uit de opgegeven lijst.\nIk denk...'
        }
        return fmt.text(fmt.hbold(messages[self.user.native_language]))
