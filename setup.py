#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import setuptools
import sys
try:
    import versioneer
except Exception:
    print "versioneer is mandatory, install it with 'pip install versioneer'"
    sys.exit(1)

extra = {}
setup_packages = ['nose>=1.0', 'versioneer>=0.15']
install_packages = []

# with python2
if sys.version_info < (3,):
    install_packages.append('telnetlib')

# with python >= 3
if sys.version_info >= (3,):
    extra['use_2to3'] = True
    install_packages.append('telnetlib3')


# Define setup
# noinspection PyPep8,PyPep8
setuptools.setup(
    name='funicular',
    setup_requires=setup_packages,
    install_requires=install_packages,
    package_dir={'': 'src'},
    packages=setuptools.find_packages('src'),
    url='',
    license='MIT',
    author='Fabien ZARIFIAN',
    author_email='fabien.zarifian@nuevolia.fr',
    description='Browser automation backend made easy !',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    **extra
)
