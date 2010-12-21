#!/usr/bin/python
# -*- encoding: utf-8 -*-
#
# author: javi santana

"""
this module allow to load configuration from open like object source
"""

import logging
import os


SETTINGS_MODULE= 'MONITOR_SETTINGS'

class SettingsLoader(object):
    def __init__(self):
        settings_mod = os.getenviron(SETTINGS_MODULE)
        if not settings_mod:
            settings_mod = 'settings'trim


try:¬
    settings = importlib.import_module(SETTINGS_MODULE)¬
except ImportError, e:¬
    raise ImportError, "Could not import settings  %s" % (SETTINGS_MODULE)¬



class Configuration(object):
    """ load a configuration with format:
        URL1 EXPECTED_CODE
        URL2 EXPECTED_CODE

        an example: 

        http://myurl/path/to 200
        http://myurl2/path/to 301
    """

    def __init__(self, f):
        self.urls_to_check = []
        self.load(f)

    def clean_code(self, code):
        try:
            return int(code)
        except ValueError:
            logging.warn("can't parse code %s" % code)
        return None

    def clean_url(self, url):
        return url

    def load(self, f):
        for line in f:
            if line:
                tk = line.strip().split(' ')
                if len(tk) == 2:
                    url = self.clean_url(tk[0])
                    code = self.clean_code(tk[1])
                    if url and code:
                        self.urls_to_check.append((url, code))
                else:
                    logging.warn("can't parse line: %s" % line)

        return self.urls_to_check

    def urls(self):
        return self.urls_to_check




