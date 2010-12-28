from distutils.core import setup

setup(name='pony_monitor', 
      author = 'Javi Santana', 
      author_email = 'jsantana@wtelecom.es',
      description = 'monitor a url for a response code',
      url='https://github.com/wellnesstelecom/pony_monitor',
      version='0.1',
      scripts=['ponymonitor.py'],
      packages=['pony_monitor','pony_monitor.backend'],
      requires = ['importlib']
)
