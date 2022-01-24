Usage
=====

.. _installation:

Installation
------------

You can install ``brawlpy`` using pip:

.. code-block:: console

   pip install brawlpy

Quick Example
----------------

To get a player by their tag:
.. autofunction:: brawlpy.Client.get_player

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

