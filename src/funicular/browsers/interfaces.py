#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# funicular.browsers.interfaces - Define interfaces on this package
#


from funicular.interfaces import IFunicularBase


class IFunicularBrowserProfiles(IFunicularBase):
    pass


class IFunicularBrowserProfile(IFunicularBase):
    pass


class IFunicularBrowserExtensions(IFunicularBase):
    pass


class IFunicularBrowserExtension(IFunicularBase):
    pass


class IFunicularBrowserConnector(IFunicularBase):
    def connect(self):
        raise NotImplemented("connect must be defined")


    def disconnect(self):
        raise NotImplemented("disconnect must be defined")


    def __del__(self):
        if self._connector:
            logger.debug('%s : disconnect' % (str(self),))
            self.disconnect()