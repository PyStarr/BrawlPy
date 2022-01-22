import brawlpy
import asyncio

client = brawlpy.Client('your_token_here') # Enter your token here

async def brawlPy():
    club = await client.get_club("JP20RUR2")
    
    print(club)

    print(club.name,club.tag, club.trophies)
    
    for member in club.members:
    
        print(member)
    
    print(club.description)
    
loop = asyncio.get_event_loop()
loop.run_until_complete(brawlPy())