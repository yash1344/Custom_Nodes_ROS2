from setuptools import find_packages
from setuptools import setup

setup(
    name='custom_interface',
    version='0.0.0',
    packages=find_packages(
        include=('custom_interface', 'custom_interface.*')),
)
