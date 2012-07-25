#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = 'django-dynamic-formset',
    version = '0.1',
    description = "jQuery plugin for dynamically adding new forms to a rendered django formset",
    long_description = open('README.txt').read(),
    author = 'Stanislaus Madueke',
    author_email = 'stan.madueke@gmail.com',
    url='http://github.com/dekkers/django-dynamic-formset/',
    packages = find_packages(),
    include_package_data = True,
    license = "BSD License",
    keywords = "django jquery formset",
    platforms = ['any'],
)
