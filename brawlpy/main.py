import imp
from xml.dom import NotFoundErr

from discord import NotFound
from itsdangerous import exc
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
            
            return data, status
            
            

    async def get_player(self,tag):
        """Get a player by tag"""

        Tag = checkTag(tag)
        
        url = self.api.PLAYER.format(playerTag=Tag)

        player, status = await self.request(url)
        if 300 > status >= 200:
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

        elif status == 403:
            raise Forbidden(status, url, url['message'])
        elif status == 404:
            raise TagNotFoundError(status)
        elif status == 429:
            raise RateLimitError(status, url)
        elif status == 500:
            raise UnexpectedError(status, url)
        elif status == 503:
            raise ServerError(status, url)

    async def get_club(self,tag):
        """Get a club by tag"""

        Tag = checkTag(tag)
        url = self.api.CLUB.format(clubTag=Tag)
        club , status= await self.request(url)

        if 300 > status >= 200:
            cc_members = []
            for each in club['members']:
                m = ClubMember(each['name'],each['icon']['id'],each['tag'],each['role'],each['nameColor'])
                cc_members.append(m)
            cl = Club(club['tag'],club['name'],club['description'],club['type'],club['badgeId'],club['requiredTrophies'],club['trophies'],cc_members)

            return cl
        
        elif status == 403:
            raise Forbidden(status, url, club['message'])
        elif status == 404:
            raise TagNotFoundError(status)
        elif status == 429:
            raise RateLimitError(status, url)
        elif status == 500:
            raise UnexpectedError(status, url, club)
        elif status == 503:
            raise ServerError(status, url)

    async def brawlers(self):
        """Get a list of all the brawlers currently in the game"""
        
        url = self.api.BRAWLERS
        brawlers, status = await self.request(url)
        if 300 > status >= 200:
            brss = brawlers[0]['items']
            brs = []
            for b in brss:
                gadgets = []
                srs = []
                
                for each in b['gadgets']:
                    gr = Gadget(each['name'],each['id'])
                    gadgets.append(gr)
                
                for each in b['starPowers']:
                    sr = StarPower(each['name'],each['id'])
                    srs.append(sr)

                brs.append(Brawler(b['name'],b['id'],srs,gadgets))

            return brs
        elif status == 403:
            raise Forbidden(status, url, url['message'])
        elif status == 404:
            raise BrawlerNotFound(status)
        elif status == 429:
            raise RateLimitError(status, url)
        elif status == 500:
            raise UnexpectedError(status, url)
        elif status == 503:
            raise ServerError(status, url)

    async def events(self):
        """Get the list of all the events currently in rotation"""
        
        url = self.api.EVENTS

        events, status = await self.request(url)

        if 300 > status >= 200:
            Ev = Event(events['id'],events['mode'],events['map'],events['startTime'],events['endTime'])

            return Ev
        
        elif status == 403:
            raise Forbidden(status, url, url['message'])
        elif status == 404:
            raise NotFoundErr(status, "Not Found!")
        elif status == 429:
            raise RateLimitError(status, url)
        elif status == 500:
            raise UnexpectedError(status, url)
        elif status == 503:
            raise ServerError(status, url)

    async def get_players_rankings(self,countryCode='global'):
        """Get top players rankings"""

        url = self.api.RANKINGS.format(countryCode=countryCode) + "/players"

        rankings, status = await self.request(url)

        if 300 > status >= 200:
        
            rankgs = []

            for each in rankings['items']:
                try:
                    cl = each['club']
                except KeyError:
                    cl = None
                else:
                    cl = cl['name']
                rankgs.append(PlayerRanking(each['name'],each['tag'],each['nameColor'],each['icon']['id'],each['trophies'],each['rank'],cl))

            return rankgs

        elif status == 403:
            raise Forbidden(status, url, url['message'])
        elif status == 404:
            raise NotFoundErr(status, "Not Found!")
        elif status == 429:
            raise RateLimitError(status, url)
        elif status == 500:
            raise UnexpectedError(status, url)
        elif status == 503:
            raise ServerError(status, url)

    async def get_brawlers_rankings(self,brawlerID,countryCode='global'):
        """Get top rankings based on brawlers"""

        url = self.api.RANKINGS.format(countryCode=countryCode) + "/brawlers/{}".format(brawlerID)

        rankings, status = await self.request(url)
        
        if 300 > status >= 200:
            rankgs = []

            for each in rankings['items']:
                try:
                    cl = each['club']
                except KeyError:
                    cl = None
                else:
                    cl = cl['name']
                rankgs.append(BrawlerRanking(each['tag'],each['name'],each['nameColor'],each['icon']['id'],each['trophies'],each['rank'],cl))
            
            return rankgs
        
        elif status == 403:
            raise Forbidden(status, url, url['message'])
        elif status == 404:
            raise BrawlerNotFound(status, brawlerID)
        elif status == 429:
            raise RateLimitError(status, url)
        elif status == 500:
            raise UnexpectedError(status, url)
        elif status == 503:
            raise ServerError(status, url)

    async def get_club_rankings(self,countryCode='global'):
        """Get top clubs rankings"""

        url = self.api.RANKINGS.format(countryCode=countryCode) + "/clubs"

        rankings, status = await self.request(url)

        if 300 > status >= 200:
            clubs = []

            for each in rankings['items']:
                clubs.append(ClubRanking(each['tag'],each['name'],each['badgeId'],each['trophies'],each['rank'],each['memberCount']))

            return clubs
        
        elif status == 403:
            raise Forbidden(status, url, url['message'])
        elif status == 404:
            raise CountryNotFound(status, countryCode)
        elif status == 429:
            raise RateLimitError(status, url)
        elif status == 500:
            raise UnexpectedError(status, url)
        elif status == 503:
            raise ServerError(status, url)

    async def get_club_members(self, clubTag):
        """Get members of a club"""
        
        tag = checkTag(clubTag)

        url = self.api.CLUB.format(clubTag=tag) + '/members'

        club, status = await self.request(url)

        if 300 > status >= 200:
            cc_members = []
            for each in club['items']:
                m = ClubMember(each['name'],each['icon']['id'],each['tag'],each['role'],each['nameColor'],each['trophies'])
                cc_members.append(m)

            return cc_members
        
        elif status == 403:
            raise Forbidden(status, url, url['message'])
        elif status == 404:
            raise TagNotFoundError(status)
        elif status == 429:
            raise RateLimitError(status, url)
        elif status == 500:
            raise UnexpectedError(status, url)
        elif status == 503:
            raise ServerError(status, url)
    
    async def get_brawler(self, brawlerID : int):
        """Get A brawler by id"""
        
        url = self.api.BRAWLER.format(id=brawlerID)

        b, status = await self.request(url)
        
        if 300 > status >= 200:
            gadgets = []
            srs = []
            
            for each in b['gadgets']:
                gr = Gadget(each['name'],each['id'])
                gadgets.append(gr)
            
            for each in b['starPowers']:
                sr = StarPower(each['name'],each['id'])
                srs.append(sr)

            brawl = await self.get_brawler(brawlerID)

            br = Brawler(brawl,b['name'],b['id'],srs,gadgets)

            return br
        elif status == 403:
            raise Forbidden(status, url, url['message'])
        elif status == 404:
            raise BrawlerNotFound(status, id = brawlerID)
        elif status == 429:
            raise RateLimitError(status, url)
        elif status == 500:
            raise UnexpectedError(status, url, b)
        elif status == 503:
            raise ServerError(status, url)