from distutils.core import setup
setup(
  name = 'cloudacademy',
  packages = ['cloudacademy'],
  version = '0.1',
  description = 'Python client for CloudAcademy.com API',
  author = 'Giacomo Marinangeli',
  author_email = 'giacomo@cloudacademy.com',
  url = 'https://bitbucket.org/cloudacademy/api/',
  download_url = 'https://bitbucket.org/cloudacademy/api/',
  keywords = ['cloudacademy', 'cloud', 'academy', 'api','rest'],
  classifiers = [],
  install_requires=[
      'requests >= 2.0.1',
  ],
)