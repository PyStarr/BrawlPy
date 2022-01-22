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

    print("-------------------------------------------------")

    club = await client.get_club("PVQ0RP90")
    
    print(club)
    print(club.name, club.tag, club.trophies)
    print(club.description)
    for member in club.members:
        print(member)

    print("-------------------------------------------------")

    leon = await client.get_brawler_byName('leon')
    print(leon)
    for each in leon.gadgets:
        print(each.name)
    for each in leon.starPowers:
        print(each.name)

    print("-------------------------------------------------")

    rankings = await client.get_players_rankings(limit=2) # Get top to players

    for each in rankings:
        print(each)


    # This is not even half what the wrapper can do, explore more on the docs!!

loop = asyncio.get_event_loop()
loop.run_until_complete(brawlPy())