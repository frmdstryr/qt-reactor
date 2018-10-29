#!/usr/bin/env python
import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: X11 Applications :: Qt',
    'Framework :: Twisted',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Natural Language :: English',
    'Topic :: Software Development :: Libraries :: Python Modules'
]

setup(
    name='qt-reactor',
    version='0.6',
    license='MIT',
    classifiers=classifiers,
    author='Christopher R. Wood',
    author_email='chris@leastauthority.com',
    description='Twisted Qt Integration for Qt4 and Qt5 using qtpy',
    long_description=read('README.rst'),
    url='https://github.com/frmdstryr/qt-reactor',
    packages=find_packages(),
    py_modules=['qreactor'],
    keywords=['Qt', 'twisted', 'qtpy'],
    install_requires=['twisted', 'qtpy']
)
