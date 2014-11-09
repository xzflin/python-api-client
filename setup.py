from distutils.core import setup
setup(
  name = 'cloudacademy',
  packages = ['cloudacademy'],
  version = '0.2',
  description = 'Python client for CloudAcademy.com API',
  author = 'Giacomo Marinangeli',
  author_email = 'giacomo@cloudacademy.com',
  url = 'https://github.com/cloudacademy/python-api-client',
  download_url = 'https://github.com/cloudacademy/python-api-client/archive/0.2.tar.gz',
  keywords = ['cloudacademy', 'cloud', 'academy', 'api','rest'],
  classifiers = [],
  install_requires=[
      'requests >= 2.0.1',
  ],
)