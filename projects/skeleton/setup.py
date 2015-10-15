try:
    from setuptools import setup
except ImportError:
    from distutils import setup

config = {
    'description': 'My Project',
    'author': 'My Name',
    'url': ''
    'download_url':''
    'version':'0.1'
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
