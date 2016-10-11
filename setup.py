try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Darryl Martin',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'darryl.martin@gmail.com',
    'version': '0.1',
    'install_requires': [''],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'TaskLoader'
}

setup(**config)
