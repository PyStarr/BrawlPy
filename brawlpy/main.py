from .API import API, checkTag
from .errors import *
from .utils import *

import aiohttp
import asyncio
import json

class Client:
    def __init__(self,token):

        self.TOKEN = token
        self.loop = asyncio.get_event_loop()
        self.api = API()
        self.headers = {
            'Authorization': 'Bearer {}'.format(token)
        }

        self.session = aiohttp.ClientSession(loop=self.loop,headers=self.headers)

    async def request(self,url):
        async with self.session.get(url=url) as resp:
            status = resp.status
            data = await resp.json()

            if 300 > status >= 200:
                return data
            elif status == 403:
                raise Forbidden(status, url, data['message'])
            elif status == 404:
                raise NotFoundError(status, reason='Not Found!')
            elif status == 429:
                raise RateLimitError(status, url)
            elif status == 500:
                raise UnexpectedError(status, url, data)
            elif status == 503:
                raise ServerError(status, url)

    async def get_player(self,tag):
        """Get a player by tag"""

        Tag = checkTag(tag)

        player = await self.request(self.api.PLAYER.format(playerTag=Tag))

        return player

    async def get_club(self,tag):
        """Get a club by tag"""

        Tag = checkTag(tag)

        club = await self.reason(self.api.CLUB.format(clubTag=Tag))

        return club

    async def brawlers(self):
        """Get a list of all the brawlers currently in the game"""
        
        brawlers = await self.request(self.api.BRAWLERS)

        return brawlers

    async def events(self):
        """Get the list of all the events currently in rotation"""
        
        events = await self.request(self.api.EVENTS)

        return events

    async def get_club_rankings(self,countryCode='global'):
        """Get top club rankings"""

        rankings = await self.request(self.api.RANKINGS.format(countryCode=countryCode) + "/clubs")

        return rankings

    async def get_players_rankings(self,countryCode='global'):
        """Get top players rankings"""

        rankings = await self.request(self.api.RANKINGS.format(countryCode=countryCode) + "/players")

        return rankings

    async def get_brawlers_rankings(self,brawlerID,countryCode='global'):
        """Get top rankings based on brawlers"""

        brawler = (getBrawlerbyID(await self.brawlers(),brawlerID))[0]

        rankings = await self.request(self.api.RANKINGS.format(countryCode=countryCode) + "/brawlers/{}".format(brawler['id']))

        return rankings

    async def get_club_rankings(self,countryCode='global'):
        """Get top clubs rankings"""

        rankings = await self.request(self.api.RANKINGS.format(countryCode=countryCode) + "/clubs")

        return rankings