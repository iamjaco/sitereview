from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sitereview',
    version='1.0',
    description='Check WebPulse categorization for any URL',
    url='https://github.com/snoopymuc/sitereview',
    author='Thomas Zäch',
    author_email='snoopymuc@gmail.com',
    packages=find_packages(),
    scripts=['sitereview.py']
)
