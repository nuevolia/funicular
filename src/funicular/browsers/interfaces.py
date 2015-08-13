#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# funicular.browsers.interfaces - Define interfaces on this package
#


from funicular.interfaces import IFunicularBase


class IFunicularBrowser(IFunicularBase):
    pass


class IFunicularBrowserProfiles(IFunicularBase):
    pass


class IFunicularBrowserProfile(IFunicularBase):
    pass


class IFunicularBrowserExtensions(IFunicularBase):
    pass


class IFunicularBrowserExtension(IFunicularBase):
    pass


class IFunicularBrowserConnector(IFunicularBase):
    pass

