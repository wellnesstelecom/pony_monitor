

Intro
-----
pony-monitor is a small tool to monitor a http server. It fetches the specified urls, checks that a valid code is returned and warns to specified email when it fails.

Quick start
-----------


**installing**

Download code:

    $ python setup.py install

You have to install importlib:

    $ sudo pip install importlib

**configuration**

pony-monitor uses the same configuration philosophy as django, it uses a settings.py file, so you have to create a settings.py file on a folder:

    #settings.py

    URLS_TO_CHECK = (
            #(URL, expected_code),
            ('http://localhost:8000/', 200),
            ('http://localhost:8000/path', 404),
    )


    # timeout in sec
    TIMEOUT = 20

    # secs
    CHECK_INTERVAL = 20

    # backend.console.ConsoleAlert is alse available
    # you can create you own backends, look inside pony_monitor.backend package
    ALERT_BACKENDS = ('backend.mail.MailAlert',)


    # email backend conf
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'YOURBOTMAIL@wtelecom.es'
    DEFAULT_FROM_EMAIL=EMAIL_HOST_USER
    EMAIL_HOST_PASSWORD = 'pass'
    EMAIL_USE_TLS = True

    # emails to be warned 
    RECIPIENTS = ['YOU@mail.com', 'johnrambot@mail.com']


**usage**

    $ vim settings.py
    $ ponymonitor.py

**production usage**

In production environment a tool like supervisord is recommended although you can use nohup:

    $ nohup ponymonitor.py &




