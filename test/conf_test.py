#!/usr/bin/python
# -*- encoding: utf-8 -*-
#
# author: javi santana

from StringIO import StringIO
from pony_monitor.conf import Configuration

def test_load():
    s = "http://test.com/url 200\nhttp://pepe.com/ 301"
    c = Configuration(StringIO(s))
    assert len(c.urls()) == 2
    assert c.urls()[1][1] == 301

def test_load_badformed():
    s = "http://test.com/url 200\njajaj  \nhttp://pepe.com/ 301 "
    c = Configuration(StringIO(s))
    assert len(c.urls()) == 2

def test_load_cantparse():
    s = "http://test.com/url 200\njajaj 2ab\nhttp://pepe.com/ 301"
    c = Configuration(StringIO(s))
    assert len(c.urls()) == 2


