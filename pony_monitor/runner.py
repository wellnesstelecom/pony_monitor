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
import time

# internal imports
from monitor import Monitor

DEFAULT_TIMEOUT = 20
DEFAULT_INTERVAL = 120

def main():
    from conf import settings

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s %(message)s',
                        stream=sys.stdout);

    timeout = getattr(settings, 'TIMEOUT', DEFAULT_TIMEOUT)
    check_time = getattr(settings, 'CHECK_INTERVAL', DEFAULT_INTERVAL)

    monitor = Monitor(settings.ALERT_BACKENDS, timeout)

    try: 
        while True:
            monitor.check(settings.URLS_TO_CHECK)
            time.sleep(check_time)
    except KeyboardInterrupt:
        pass
    except Exception, e:
        logging.error(e)

if __name__ == '__main__':
    main()

