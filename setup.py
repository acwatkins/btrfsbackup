#!/usr/bin/env python3

from setuptools import setup

setup(name='btrfsbackup',
      version='0.0.0.1',
      description='A snapshot/backup script for btrfs',
      url='https://github.com/acwatkins/btrfsbackup',
      author='Adam Watkins',
      author_email='acwatkins@gmail.com',
      license='GPL3',
      scripts=['bin/btrfsbackup'])
