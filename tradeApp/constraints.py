MAX_TITLE_LENGTH = 500
MAX_DESCRIPTION_LENGTH = 10_000
MAX_NAME_SIZE = 200
OBJECTS_PER_PAGE = 20
SHORT_TEXT_SIZE = 50
SHORT_TEXT_ENDING = '...'


def get_short_text(text: str):
    if len(text) > SHORT_TEXT_SIZE:
        return f'{text[:SHORT_TEXT_SIZE - len(SHORT_TEXT_ENDING)]}{SHORT_TEXT_ENDING}'

    return text
