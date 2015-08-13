#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import sys
try:
    import versioneer
except Exception as e:
    print("versioneer is mandatory, install it with 'pip install versioneer':\n" % (e.message,))
    sys.exit(1)

extra = {}
setup_packages = ['nose>=1.0']
install_packages = []

# with python2
if sys.version_info < (3,):
    extra['use_2to3'] = False

# with python >= 3
if sys.version_info >= (3,):
    extra['use_2to3'] = True

# Define setup
# noinspection PyPep8,PyPep8
setuptools.setup(
    name='funicular',
    setup_requires=setup_packages,
    install_requires=install_packages,
    package_dir={'': 'src'},
    packages=setuptools.find_packages('src'),
    url='http://funicular.readthedocs.org/',
    license='MIT',
    author='Fabien ZARIFIAN',
    author_email='fabien.zarifian@nuevolia.fr',
    description='Browser automation made easy !',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    use_2to3=extra['use_2to3']
)
