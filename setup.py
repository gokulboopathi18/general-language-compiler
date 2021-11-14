'''
    libGLC setup script
'''

from setuptools import find_packages, setup

setup(
    name='libGLC',
    version='1.0.0',
    packages=find_packages('./'),
    entry_points = {
        'console_scripts': [
            'libGLC = libGLC.__main__:main'
        ]
    }
)