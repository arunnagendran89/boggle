import uuid
from random import randint

def get_unique_id():
    project_name = 'BoggleProject'
    return uuid.uuid3(uuid.NAMESPACE_DNS, project_name)


def get_random_character():
    start_char_ord = 97  # ordinal of char 'a' in ASCII table
    end_char_ord = 122  # ordinal of char 'x' in ASCII table
    return chr(randint(start_char_ord, end_char_ord))

