#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# author: javi santana

import sys
import os
from pony_monitor.runner import main

sys.path.append(os.getcwd())

os.environ['PONY_SETTINS_MODULE'] = 'settings'

if __name__ == '__main__':
    main()
