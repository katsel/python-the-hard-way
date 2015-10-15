try:
    from setuptools import setup
except ImportError:
    from distutils import setup

config = {
    'description': 'Learn Python The Hard Way - Exercise 48',
    'author': 'Katharina',
    'url': 'http://learnpythonthehardway.org/book/ex48.html'
    'download_url':''
    'version':'0.1'
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'scripts': [],
    'name': 'ex48'
}

setup(**config)
