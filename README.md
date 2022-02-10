# BrawlPy
<a href="https://pypi.org/project/brawlpy">
    <img alt="Downloads" src="https://img.shields.io/pypi/dm/brawlpy?color=blue">
</a>
<a href="https://pypi.org/project/brawlpy">
    <img alt="PyPI" src="https://img.shields.io/pypi/v/brawlpy?color=blue">
</a>

A basic wrapper for the [Brawl Stars API](https://developer.brawlstars.com/#/).

## Features
 * Easy to use with OOP design
 * Get a player's profile and battle log by just a tag
 * Get a club and all its member
 * Get the top 200 clubs , players, or a specific brawler in the world or a region
 * Get Information about a map, event, brawler!!!

## Installation
To install the library run the following command:
```
pip install brawlpy
```
To install the development version run the following command:
```
pip install git+https://github.com/PyStarr/BrawlPy
```

## Example
A Simple Example to get a player by their tag
```py
import brawlpy
import asyncio

client = brawlpy.Client('your_api_key_here') # Enter your api key here

async def main():
    player = await client.get_player("JP20RUR2")
    
    print(player)

    print(player.name, player.tag, player.trophies)

asyncio.run(main())
```
Another simple Example to get a club by its tag
```py
import brawlpy
import asyncio

client = brawlpy.Client('your_api_key_here') # Enter your api key here

async def brawlPy():
    club = await client.get_club("PVQ0RP90")
    
    print(club)

    print(club.name, club.tag, club.trophies)
    
    print(club.description)
    
asyncio.run(brawlPy())
```
