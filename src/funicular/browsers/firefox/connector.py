#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# funicular.interfaces.browsers.firefox.connector - Define Firefox connector
#

import telnetlib
import argparse
import logging
import re

from funicular.browsers.interfaces import IFunicularBrowserConnector


class FirefoxConnector(IFunicularBrowserConnector):
    def __init__(self, hostname='localhost', port=4242, timeout=5, logger=logging.getLogger(__name__)):
        self.hostname = hostname
        self.port = port
        self.timeout = timeout
        self.logger = logger
        self.instance_name = b'repl'
        self._record_separator = b'\r\n'
        self._telnet = telnetlib.Telnet()

    def connect(self):
        self._telnet.open(self.hostname, self.port, self.timeout)
        motd = self._telnet.read_until(self._get_prompt(), 1)
        if not motd.endswith(self._get_prompt()):
            match = re.search(br'(repl\d+)>', motd)
            if match:
                self.logger.debug('instance = %s' % (match.group(1),))
                self.instance_name = match.group(1)

    def disconnect(self):
        self.execute('%s.close();' % (self.instance_name,), get_response=False)
        self._telnet.close()
        delattr(self, '_telnet')

    def execute(self, command, timeout=5, get_response=True):
        self.logger.debug('%s' % (command,))
        self._telnet.write('%s%s' % (command, self._record_separator))
        if get_response:
            result = self._telnet.read_until(self._get_prompt(), timeout)
            result = result \
                .replace(self._get_prompt(), '') \
                .rstrip()
            self.logger.debug('result : %s' % (result,))
        else:
            result = 'done'
        return result

    def _get_prompt(self):
        return b'%s>' % (self.instance_name,)

    def __str__(self):
        return '<%s: hostname=%s, port=%s, instance=%s>' % (type(self), self.hostname, self.port, self.instance_name)

    def __del__(self):
        if self._telnet:
            logger.debug('close telnet')
            self.disconnect()


if __name__ == '__main__':

    # Configuration des paramètres
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", help="debug mode", action="store_true")
    parser.add_argument("-u", "--load", help="url to load", default="http://www.google.fr")
    parser.add_argument("-p", "--png", help="png to save", default="out.png")
    parser.add_argument("-t", "--timeout", help="timeout in seconds", default=5)

    # Récupération des paramètres
    args = parser.parse_args()

    # Initialisation du logger
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.WARNING)
    logger = logging.getLogger(__name__)

    connector = FirefoxConnector(timeout=10, logger=logger)
    connector.connect()
    connector.execute('%s.look();' % (connector.instance_name,))
    connector = None
