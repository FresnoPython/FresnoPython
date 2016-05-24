============
FresnoPython
============

.. image:: https://travis-ci.org/dmpayton/FresnoPython.svg?branch=master
    :target: https://travis-ci.org/dmpayton/FresnoPython

**Version**: 1.0.0

**License**: MIT

Usage
=====

Library
-------

.. code-block:: python

    >>> import FresnoPython

    >>> FresnoPython.website
    'http://FresnoPython.com'

    >>> FresnoPython.next_meeting_date()
    datetime.datetime(2016, 5, 24, 18, 30)

    # etc...

Command-line
------------

.. code-block::

    usage: fresno.py [-h] [--website] [--map] [--twitter]

    Process some integers.

    optional arguments:
      -h, --help  show this help message and exit
      --website   Open the website.
      --map       Open the location on Google Maps.
      --twitter   Open the twitter account.


.. notes::

    Release process:

    1. Update version info
     * README.rst
     * setup.py

    2. git tag -a vX.Y.Z -m 'Version X.Y.Z'

    3. Upload to PyPI:
     * python setup.py sdist upload
     * python setup.py bdist_wheel upload
