from distutils.core import setup

setup(name='pony_monitor', 
      author = 'Javi Santana', 
      author_email = 'jsantana@wtelecom.es',
      description = 'monitor a url for a response code',
      version='0.1',
      packages=['pony_monitor'],
      requires = ['importlib']
)
