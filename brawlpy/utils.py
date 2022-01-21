from .errors import *

async def getBrawlerbyName(brawlers,brawlerName):
    """Get a brawler by its Name"""
    
    brs = (brawlers['items'])

    brawler = [i for i in brs if i['name'] == brawlerName]

    if not brawler:
        raise BrawlerNotFound(404, name=brawlerName)
    elif brawler:
        return brawler

async def getBrawlerbyID(brawlers, brawlerID : int):
    """Get a brawler by its ID"""
    
    brs = (brawlers['items'])

    brawler = [i for i in brs if i['id'] == brawlerID]

    if not brawler:
        raise BrawlerNotFound(404, id=brawlerID)
    elif brawler:
        return brawler