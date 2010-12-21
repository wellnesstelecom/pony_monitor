#!/usr/bin/python
# -*- encoding: utf-8 -*-
#
# author: javi santana

"""
"""

import logging
import importlib


SETTINGS_MODULE= 'settings'

# ripped from django code
try:
    settings = importlib.import_module(SETTINGS_MODULE)
except ImportError, e:
    raise ImportError, "Could not import settings  %s" % (SETTINGS_MODULE)






