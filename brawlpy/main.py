from .API import API, checkTag
from .errors import *

import aiohttp
import asyncio

class Client:
    def __init__(self,token):

        self.TOKEN = token
        self.loop = asyncio.get_event_loop()
        self.api = API()

        self.session = aiohttp.ClientSession(loop=self.loop)