__author__ = 'lobocv'

from distutils.core import setup
from crashreporter import __version__

setup(
    name='crashreporter',
    packages=['crashreporter'],  # this must be the same as the name above
    version=__version__,
    description='Track and send crash reports by email or FTP',
    author='Calvin Lobo',
    author_email='calvinvlobo@gmail.com',
    url='https://github.com/lobocv/crashreporter',
    download_url='https://github.com/lobocv/crashreporter/tarball/%s' % __version__,
    keywords=['crash', 'reporting', 'testing', 'debugging', 'bugs'],
    classifiers=[],
    requires=['jinja2 >= 2.7.3']
)