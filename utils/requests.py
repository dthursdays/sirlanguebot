import openai

from data import config
from data.languages import languages
from utils.additional import remove_tags

tags_to_remove = ["br", "ul", "li", "h1"]


async def analysis(words, language_to_learn, native_language):
    language_to_learn = languages.get(language_to_learn)
    native_language = languages.get(native_language)
    openai.api_key = config.GPT_TOKEN

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content":
                f'\n1. Write "{words}" in {language_to_learn}'
                f'\n2. Give me the transcription and a link to the pronunciation record for {language_to_learn}.'
                f'\n3. Give me most popular meanings in {language_to_learn}, for every meaning give me a link to google image search, '
                f'explanation in {language_to_learn} and {native_language} translation of the explanation.'
                f'\nFor whole the text use <b> or <i> tags to make the text convenient to read and use <a href="link">text</a> for every link.'
                f'\nAll the comments give in {native_language}.'},
        ],
        temperature=0.3,
        max_tokens=3000
    )

    if response and response.choices:
        return remove_tags(response.choices[0].message.content, tags_to_remove)

    else:
        return None


async def story(words, language_to_learn, native_language):
    language_to_learn = languages.get(language_to_learn)
    native_language = languages.get(native_language)
    openai.api_key = config.GPT_TOKEN

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {
                "role": "system",
                "content": f'"{words}"'
                           f'\nIf the text above contains non-{language_to_learn} words, firstly, translate them to {language_to_learn}.'
                           f'\nWith the words you now have create '
                           f'a short tale of 4-5 sentences in {language_to_learn} that '
                           f'contains most of them. Please avoid advanced grammatical '
                           f'construction as well as rare words and phrases.'
                           f'\nAlso create {native_language} translation, - translate the words accordingly '
                           f'to the story context and do not be afraid to express yourself.'
                           f'\nAlso make the tale name bold (use html).'
            }
            ],
        max_tokens=3000,
        temperature=0.7
    )

    if response and response.choices:
        return remove_tags(response.choices[0].message.content, tags_to_remove)

    else:
        return None


async def translate(words, language_to_learn, native_language):
    language_to_learn = languages.get(language_to_learn)
    native_language = languages.get(native_language)
    openai.api_key = config.GPT_TOKEN

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": f'"{words}"'
                f'\nGive {language_to_learn} and {native_language} version of the phrase(s) above.'
                f'\nYou are a extra charismatic medieval knight: give a comment on the topic of the phrase(s) in {language_to_learn} language without translation.'
                f'\nDon\'t mention anything about your role. Mark your comment just with "- ".'},
        ],
        temperature=0.3,
        max_tokens=3000
    )

    if response and response.choices:
        return remove_tags(response.choices[0].message.content, tags_to_remove)

    else:
        return None
