#!/usr/bin/env python

import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

packages = ['sellsy_client']

requires = [
    'requests>=2.18.4',
    'requests-oauthlib>=0.8.0'
]

about = {}
with open(os.path.join(here, 'sellsy_client', '__version__.py'), mode='r', encoding='utf-8') as f:
    exec(f.read(), about)

setup(
    name = about['__title__'],
    version = about['__version__'],

    packages = packages,
    install_requires = requires,  

    author = about['__author__'],
    description = about['__description__'],
    url = about['__url__'],
    license = about['__license__'],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Licence :: OSI Appouved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords = 'Sellsy SellsyAPI SellsyClient sellsy_client',
    project_urls = {
        'Bug Reports': 'https://github.com/Annouar/sellsy-client/issues'
    }
)