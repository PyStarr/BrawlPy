from .API import API, checkTag
from .errors import *

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

        self.session = aiohttp.ClientSession(loop=self.loop)

    async def request(self,url):
        async with self.session.get(url=url,headers=self.headers) as resp:
            res = await resp.text()
            data = json.load(res)

        return data