from .errors import *

def checkTag(tag : str):
    tag = tag.strip("#").upper()
    allowed_chars = "0289PYLQGRJCUV"

    if len(tag) < 3:
        raise TagNotFoundError(404, reason="Tag can't be less then 3 characters!")
    invalid = [i for i in tag if i not in allowed_chars]
    if invalid:
        raise TagNotFoundError(404, reason="An Invalid character has been passed!",invalid_characters=invalid)

    if not tag.startswith("%23"):
        tag = "%23" + tag

    return tag