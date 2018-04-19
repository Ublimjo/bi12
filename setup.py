#!/usr/bin/env python
import os

from setuptools import setup, find_packages


setup(
    name='bi12',
    version='0.7',
    description='Bible new world translation(NWT) in pure python',
    url='https://github.com/Ublimjo/bi12',

    author='Ublim',
    author_email='ublimjo@gmail.com',

    keywords='bi12 bible baiboly nwt jw jw.org jehovah',

    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'hues',
        'beautifulsoup4',
        'click',
        'pre-commit',
    ],
    entry_points={
        'console_scripts': [
            'bi12 = bi12.__main__:main',
        ]
    },
)


os.system('unzip FloatingBible.zip -d $PREFIX/share/bi12/')
