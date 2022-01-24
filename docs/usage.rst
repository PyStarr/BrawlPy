Usage
=====

.. _installation:

Installation
------------

You can install brawlpy using pip:

.. code-block:: console

   pip install brawlpy

or

.. code-block:: console

   pip install git+https://github.com/PyStarr/BrawlPy

for the development version

Quick Example
----------------

To start you have to first create a Client-Session with your API key :-

.. code-block:: python

   import brawlpy
   import asyncio

   client = brawlpy.Client("YOUR_API_KEY")

   async def main():
      player = await client.get_player("TAG")

   loop = asyncio.get_event_loop()
   loop.run_until_complete(main())

A Simple Example to get a player by their tag

.. code-block:: python

   player = await client.get_player("JP20RUR2")

Another simple Example to get a club by its tag

.. code-block:: python

   club = await client.get_club("PVQ0RP90")

