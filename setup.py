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
        'numpy',
        'matplotlib',
        #'scipy',  # `./setup.py install` で失敗するため、 `pip install scipy` をする。
    ],
    tests_require    = [
        'nose',
    ],
    packages         = [
        'prmlpy',
        'prmlpy.distribution',
    ],
    scripts          = [
    ],
)
