### -*- coding: utf-8 -*- ####################################################

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

version = '0.1'

install_requires = [
    'setuptools',
    'Django',
    'markdown2',
    'python-openid',
    #'mysql-python',
    'html5lib',
    'app_media',
    'django_authopenid',
    'django-extensions',
    'django-profiles',
]

extras_require = dict(
    test = ['coverage',
            'windmill',
            ]
)

#AFAIK:
install_requires.extend(extras_require['test'])

setup(
    name = "cnprog",
    version = version,
    description = "http://stackoverflow.com/ like application.",
    long_description = read('README'),
    author = 'Chen Gang',
    url = 'http://cnprog.com',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data = True,
    zip_safe = False,
    install_requires = install_requires,
    extras_require = extras_require,
    entry_points="""
      # -*- Entry points: -*-
      """,
    dependency_links = ['http://pypi.saaskit.org/app-media/',],
)