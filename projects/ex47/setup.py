try:
    from setuptools import setup
except ImportError:
    from distutils import setup

config = {
    'description': 'Learn Python The Hard Way - Exercise 47',
    'author': 'Katharina',
    'url': 'http://learnpythonthehardway.org/book/ex47.html'
    'download_url':''
    'version':'0.1'
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'ex47'
}

setup(**config)
