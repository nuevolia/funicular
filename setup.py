#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import setuptools
import sys

extra = {}
try: 
    import versioneer
    extra['version']=versioneer.get_version()
    extra['cmdclass']=versioneer.get_cmdclass()
except Exception:
    print "versioneer is mandatory, install it with 'pip install versioneer'"
    sys.exit(1)

# 2to3 if python >= 3
if sys.version_info >= (3,):
    extra['use_2to3'] = True

# Define setup
# noinspection PyPep8,PyPep8
setuptools.setup(
    name='funicular',
    setup_requires=['nose>=1.0', 'versioneer>=0.15'],
    package_dir={'': 'src'},
    packages=setuptools.find_packages('src'),
    install_requires=['telnetclient'],
    url='',
    license='MIT',
    author='Fabien ZARIFIAN',
    author_email='fabien.zarifian@nuevolia.fr',
    description='Browser automation backend made easy !',
    **extra
)
