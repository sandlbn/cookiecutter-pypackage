#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name=u'{{ cookiecutter.repo_name }}',
    version=u'{{ cookiecutter.version }}',
    description=u'{{ cookiecutter.project_short_description }}',
    long_description=readme + u'\n\n' + history,
    author=u'{{ cookiecutter.full_name }}',
    author_email=u'{{ cookiecutter.email }}',
    url=u'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages=[
        u'{{ cookiecutter.repo_name }}',
    ],
    package_dir={u'{{ cookiecutter.repo_name }}': u'{{ cookiecutter.repo_name }}'},
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords=u'{{ cookiecutter.repo_name }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
)
