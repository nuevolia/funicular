#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# funicular.interfaces.browsers.firefox.connector - Define Firefox connector
#
from funicular.browsers.interfaces import IFunicularBrowserConnector
import telnetlib
import re


class FirefoxConnector(IFunicularBrowserConnector):
    def __init__(self, hostname='localhost', port=4242, timeout=5, logger=logger):
        self.hostname = hostname
        self.port = port
        self.timeout = timeout
        self._logger = logger or logging.getLogger(__name__)
        self._instance_name = b'repl'
        self._record_separator = b'\r\n'
        self._connector = telnetlib.Telnet()
        self._rx_prompt = br'(repl\d+)>'

    def connect(self):
        self._connector.open(self.hostname, self.port, self.timeout)
        motd = self._connector.read_until(self._get_prompt(), 1)
        if not motd.endswith(self._get_prompt()):
            match = re.search(self._rx_prompt, motd)
            if match:
                self._logger.debug('instance = %s' % (match.group(1),))
                self._instance_name = match.group(1)

    def disconnect(self):
        self.execute('%s.close();' % (self._instance_name,), get_response=False)
        self._connector.close()
        delattr(self, '_telnet')

    def execute(self, command, timeout=5, get_response=True):
        self._logger.debug('%s' % (command,))
        self._connector.write('%s%s' % (command, self._record_separator))
        if get_response:
            result = self._connector.read_until(self._get_prompt(), timeout)
            result = result \
                .replace(self._get_prompt(), '') \
                .rstrip()
            self._logger.debug('result : %s' % (result,))
        else:
            result = 'done'
        return result

    def _get_prompt(self):
        return b'%s>' % (self._instance_name,)

    def __str__(self):
        return '<%s: hostname=%s, port=%s, instance=%s>' % (type(self), self.hostname, self.port, self._instance_name)



if __name__ == '__main__':

