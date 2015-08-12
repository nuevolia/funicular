# -*- coding: utf-8 -*-
import telnetlib
import argparse, logging, re

class DefaultBrowser(object):
    """
    Default browser class
    """
    def __init__(self, *args, **kwargs):
        self.command = None

class ProfilesFactory(object):
    def __init__(self):




class DefaultProfile(object):
    def __init__(self):
        self.name = None

    def add_extension:(self, name):
        pass

class Firefox(DefaultBrowser):

class FirefoxApplication(object):
    pass

class FirefoxApplicationAPI35(FirefoxApplication):
    pass

class FirefoxApplicationAPI36(FirefoxApplicationAPI35):
    pass

class FirefoxApplicationAPI40(FirefoxApplicationAPI36):
    pass


class MozReplClient(object):
    def __init__(self, hostname='localhost', port=4242, timeout=5, logger=logging.getLogger(__name__)):
        self.hostname = hostname
        self.port = port
        self.timeout = 5
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
                self.logger.debug('instancename = %s' % (match.group(1),))
                self.instance_name = match.group(1)

    def disconnect(self):
        self.execute('%s.close();' % (self.instance_name,), get_response=False)
        self._telnet.close()


    def execute(self, command, timeout=5, get_response=True):
        self.logger.debug('%s' % (command, ))
        self._telnet.write('%s%s' % (command, self._record_separator))
        if get_response:
            result = self._telnet.read_until(self._get_prompt(), timeout)
            result = result\
                        .replace(self._get_prompt(), '')\
                        .rstrip()
            self.logger.debug('result : %s' % (result, ))
        else:
            result = "done"
        return result

    def _get_prompt(self):
        return b'%s>' % (self.instance_name, )

    def __str__(self):
        return '%s: hostname=%s, port=%s, instance=%s' % (type(self), self.hostname, self.port, self.instance_name)

    def __del__(self):
        if self._telnet:
            logger.debug('close telnet')
            self.disconnect()
            delattr(self, '_telnet')



if __name__ == '__main__':

    # Configuration des paramètres
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", help="debug mode", action="store_true")
    parser.add_argument("-u", "--url", help="url to load", default="http://www.google.fr")
    parser.add_argument("-p", "--png", help="png to save", default="out.png")
    # Récupération des paramètres
    args = parser.parse_args()

    # Initialisation du logger
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.WARNING)
    logger = logging.getLogger(__name__)

    client = MozReplClient(logger=logger)
    client.connect()
    client.execute('%s.look();' % (client.instance_name,))
    client = None
