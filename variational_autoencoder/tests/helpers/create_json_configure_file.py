"""version 0.1.1"""
import json
import random
import string
from .create_configure_dict import create_configure_dict


def create_json_configure_file(filename: str, is_json_syntax_good=True) -> dict:
    """
    Creates json file with example configure. If is_json_syntax_good is False,
    some syntax mistake will be add.

    Parameters
    ----------
    filename: str
    is_json_syntax_good: bool = True

    Returns
    -------
    dict
    """
    configure_dict = create_configure_dict()

    json_string = json.dumps(configure_dict, indent=4)

    if is_json_syntax_good is False:
        characters = string.ascii_letters + string.digits
        random_string_length = 20
        random_string = "".join(random.choice(characters) for _ in range(random_string_length))

        json_string += random_string

    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(json_string)

    if is_json_syntax_good:
        return configure_dict
    return None
