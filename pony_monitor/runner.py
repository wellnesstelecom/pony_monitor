#!/usr/bin/python
# -*- encoding: utf-8 -*-
#
# author: javi santana

"""
monitor runner. Check for specified urls and alert when somthing fail
"""

# python imports 
import sys
import logging
from urllib2 import urlopen

# internal imports
from conf import Configuration

def run(conf_file):
    conf = Configuration()
    urls_to_check = conf.urls_to_check()
    for url, expected_code in urls_to_check:
        ret_code = urlopen(url).getcode() 
        if ret_code != expected_code:
            logging.info("check %s FAILED! code %d" % (url, code))
            logging.info("sending alert")



if __name__ == '__main__':
    if len(sys.argv) >= 2:
        run(sys.argv[1])
    

