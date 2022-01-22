import imp
from .API import API, checkTag
from .errors import *
from .utils import *

import aiohttp
import asyncio
import json
from .Objects import *

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
        c = player['club']
        if len(c) < 1:
            cl = None
        else:
            cc = await self.get_club(c['tag'])
            cc_members = []
            for each in cc['members']:
                m = ClubMember(each['name'],each['icon']['id'],each['tag'],each['role'],each['nameColor'])
                cc_members.append(m)
            cl = Club(cc['tag'],cc['name'],cc['description'],cc['type'],cc['badgeId'],cc['requiredTrophies'],cc['trophies'],cc_members)
        
        brs = player['brawlers']
        brrs = []
        for each in brs:
            grs = []
            srs = []
            gears = []
            for i in each['gadgets']:
                gr = Gadget(i['name'],i['id'])
                grs.append(gr)
            for i in each['starPowers']:
                sr = StarPower(i['name'],i['id'])
                srs.append(sr)
            for i in each['gears']:
                gear = Gear(i['name'],i['id'],i['level'])
                gears.append(gear)

            br = PlayerBrawler(each['name'],each['id'],each['power'],each['rank'],each['trophies'],each['highestTrophies'],grs,gears,srs)
            brrs.append(br)

        Pl = Player(player['name'],player['tag'],player['nameColor'],player['icon']['id'],player['trophies'],player['expLevel'],player['expPoints'],cl,player['highestTrophies'],player['soloVictories'],player['duoVictories'],player['3vs3Victories'],player['bestRoboRumbleTime'],player['bestTimeAsBigBrawler'],brrs)

        return Pl

    async def get_club(self,tag):
        """Get a club by tag"""

        Tag = checkTag(tag)

        club = await self.request(self.api.CLUB.format(clubTag=Tag))

        cc_members = []
        for each in club['members']:
            m = ClubMember(each['name'],each['icon']['id'],each['tag'],each['role'],each['nameColor'])
            cc_members.append(m)
        cl = Club(club['tag'],club['name'],club['description'],club['type'],club['badgeId'],club['requiredTrophies'],club['trophies'],cc_members)

        return cl

    async def brawlers(self):
        """Get a list of all the brawlers currently in the game"""
        
        brawlers = await self.request(self.api.BRAWLERS)

        brss = brawlers['items']
        gadgets = []
        srs = []
        
        for each in brss['gadgets']:
            gr = Gadget(each['name'],each['id'])
            gadgets.append(gr)
        
        for each in brss['starPowers']:
            sr = StarPower(each['name'],each['id'])
            srs.append(sr)

        Brs = Brawler(brawlers['name'],brawlers['id'],srs,gadgets)

        return Brs

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

    async def get_club_members(self, clubTag):
        """Get members of a club"""

        club = await self.request(self.api.CLUB.format(tag=clubTag) + '/members')

        return club