#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
import re

try:
    import setuptools
    setup = setuptools.setup
except ImportError:
    setuptools = None
    from distutils.core import setup

packages = [
    'sms',
    'sms.backends',
    'sms.conf',
    'sms.migrations',
]

setup(
    name = 'django-send-messages',
    version = '1.0.1',
    description = 'A simple API to send messages, includes Yunpian backend and Wechat(weixin) backend.',
    long_description=open('README.md').read(),
    author='Leon Liu',
    author_email='liuyong@hwbuluo.com',
    maintainer_email='liuyong@hwbuluo.com',
    license='BSD',
    url='https://github.com/hwbuluo/django-send-messages',
    platforms='any',
    packages=packages,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=['Django'],
)

