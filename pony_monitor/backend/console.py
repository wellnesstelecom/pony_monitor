#!/usr/bin/python
# -*- encoding: utf-8 -*-
#
# author: javi santana

import logging

class ConsoleAlert(object):

    def alert(self, url, expected_code, code):
        """ called when a check fails. If code is None http server can't be reqached """
        if code:
            logging.error("ALERT %s returned %d, expected %d" % (url, expected_code, code))
        else:
            logging.error("ALERT failed to connect to %s" % url)

    def back_to_normal(self, url, code):
        logging.info("Back to normal %s" % url)
