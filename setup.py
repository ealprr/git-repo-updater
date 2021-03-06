# -*- coding: utf-8  -*-
#
# Copyright (C) 2011-2014 Ben Kurtovic <ben.kurtovic@gmail.com>
# See the LICENSE file for details.

import sys

from setuptools import setup, find_packages

if sys.hexversion < 0x02070000:
    exit("Please upgrade to Python 2.7 or greater: <http://python.org/>.")

from gitup import __version__

with open('README.md') as fp:
    long_desc = fp.read()

setup(
    name = "gitup",
    packages = find_packages(),
    entry_points = {"console_scripts": ["gitup = gitup.script:run"]},
    install_requires = ["GitPython >= 0.3.6", "colorama >= 0.3.3"],
    version = __version__,
    author = "Ben Kurtovic",
    author_email = "ben.kurtovic@gmail.com",
    description = "Easily pull to multiple git repositories at once.",
    long_description = long_desc,
    license = "MIT License",
    keywords = "git repository pull update",
    url = "http://github.com/earwig/git-repo-updater",
    classifiers = [
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Version Control"
    ]
)
