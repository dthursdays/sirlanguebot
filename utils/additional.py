import re


def remove_tags(text, tags):
    for tag in tags:
        pattern = re.compile(f'<{tag}.*?>|</{tag}>')
        text = re.sub(pattern, '', text)
    return text


def truncate_string(text, max_length):
    if len(text) <= max_length:
        return text

    truncated_text = text[:max_length]
    last_space_index = truncated_text.rfind(' ')

    if last_space_index != -1:
        truncated_text = truncated_text[:last_space_index]

    return truncated_text
