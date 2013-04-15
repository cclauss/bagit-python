from sys import version, exit
from setuptools import setup

if version < '3.3.0':
    print "python 3.3 is required"
    exit(1)

description = \
"""
This package can be used to create BagIt style packages of
digital content for safe transmission and digital preservation.
See: http://en.wikipedia.org/wiki/BagIt for more details.
"""

# for older pythons ...
requirements = []
try:
    import multiprocessing
except:
    requirements.append("multiprocessing")
try:
    import hashlib
except:
    requirements.append("hashlib")


setup(
    name = 'bagit',
    version = '1.0.2',
    url = 'http://github.com/edsu/bagit',
    author = 'Ed Summers',
    author_email = 'ehs@pobox.com',
    py_modules = ['bagit',],
    scripts = ['bagit.py'],
    description = description,
    platforms = ['POSIX'],
    test_suite = 'test',
    install_requires = requirements,
    classifiers = [
        'License :: Public Domain',
        'Intended Audience :: Developers',
        'Topic :: Communications :: File Sharing',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Filesystems',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ],
)
