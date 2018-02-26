#!/usr/bin/env python

import os
from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

packages = find_packages(exclude=('tests',))

requires = [
    'requests>=2.18.4',
    'requests-oauthlib>=0.8.0'
]

setup_requires = [
    'pytest-runner'
]

tests_require = [
    'pytest'
]

about = {}
with open(os.path.join(here, 'sellsy_client', '__version__.py'), mode='r', encoding='utf-8') as f:
    exec(f.read(), about)

with open('README.md', mode='r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name = about['__title__'],
    version = about['__version__'],

    packages = packages,
    install_requires = requires,

    tests_require = tests_require,
    setup_requires = setup_requires,

    author = about['__author__'],
    description = about['__description__'],
    long_description = readme,
    url = about['__url__'],
    license = about['__license__'],
    #classifiers = [
    #    'Development Status :: 3 - Alpha',
    #    'Intended Audience :: Developers',
    #    'Licence :: OSI Appouved :: MIT License',
    #    'Programming Language :: Python :: 3.5',
    #],
    keywords = 'Sellsy SellsyAPI SellsyClient sellsy_client',
    project_urls = {
        'Bug Reports': 'https://github.com/Annouar/sellsy-client/issues'
    }
)