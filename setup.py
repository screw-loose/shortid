from setuptools import setup, find_packages

__version__ = '0.1.0'

setup(
    name='shortid',
    version=__version__,
    description='Short id generator',
    author='Dmitry Moskowski',
    author_email='me@corpix.ru',
    url='https://github.com/corpix/shortid',
    download_url='https://github.com/corpix/shortid/archive/{0}.tar.gz'.format(__version__),
    keywords = ['short', 'id', 'uuid', 'shortid', 'tinyid'],
    packages=['shortid'],
    classifiers=[],
)
