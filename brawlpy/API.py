from .errors import *

class API:
    def __init__(self, base_url = 'https://api.brawlstars.com/v{}', version=1) -> None:
        
        self.BASE = base_url.format(version)
        self.PLAYER = self.BASE + "/players"
        self.CLUB = self.BASE + "/clubs"
        self.RANKINGS = self.BASE + "/rankings"
        self.BRAWLERS = self.BASE + "/brawlers"

def checkTag(tag : str):
    tag = tag.strip("#").upper()
    allowed_chars = "0289PYLQGRJCUV"

    if len(tag) < 3:
        raise NotFoundError(404, reason="Tag can't be less then 3 characters!")
    invalid = [i for i in tag if i not in allowed_chars]
    if invalid:
        raise NotFoundError(404, reason="An Invalid character has been passed!",invalid_characters=invalid)

    if not tag.startswith("%23"):
        tag = "%23" + tag

    return tag