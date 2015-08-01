#!/usr/bin/env python
from setuptools import setup


setup(
    name             = 'prml-python',
    description      = 'Playground. Toys from PRML.',
    long_description = open('README.md').read(),
    url              = 'https://github.com/laysakura/prml-python',
    # license          = 'LICENSE.txt',
    # version          = '2.2.2',
    author           = 'Sho Nakatani',
    author_email     = 'lay.sakura@gmail.com',
    install_requires = [
    ],
    tests_require    = [
        'nose',
    ],
    packages         = [
        'prmlpy',
    ],
    scripts          = [
    ],
)
