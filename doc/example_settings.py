#!/usr/bin/python
# -*- encoding: utf-8 -*-
#
# author: javi santana



URLS_TO_CHECK = (
        ('http://localhost:8000/', 200),
        )


# timeout in sec
TIMEOUT = 20

# secs
CHECK_INTERVAL = 20

ALERT_BACKENDS = ('pony_monitor.backend.mail.MailAlert',)


# email backend conf
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mail@mail.es'
DEFAULT_FROM_EMAIL=EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True

RECIPIENTS = ['user@mail.com']
