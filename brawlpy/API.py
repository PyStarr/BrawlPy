from .errors import *

class API:
    def __init__(self, base_url = 'https://api.brawlstars.com/v{}', version=1) -> None:
        
        self.BASE = base_url.format(version)
        self.PLAYER = self.BASE + "/players"
        self.CLUB = self.BASE + "/clubs"
        self.RANKINGS = self.BASE + "/rankings"
        self.BRAWLERS = self.BASE + "/brawlers"

def convertTag(tag : str):
    tag = tag.strip("#").upper()