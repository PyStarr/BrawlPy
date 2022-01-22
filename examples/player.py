import brawlpy
import asyncio

client = brawlpy.Client('your_token_here') # Enter your token here

async def brawlPy():
    player = await client.get_player("JP20RUR2")
    
    print(player)

    print(player.name,player.tag, player.trophies)
    
    for brawler in player.brawlers:
    
        print(brawler)
    
    print(player.club) # returns None cuz I am not in a club :( , try changing the tag

    
loop = asyncio.get_event_loop()
loop.run_until_complete(brawlPy())