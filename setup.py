from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='pranali_reloaded',
    version=version,
    description='A reporting system for Rotaract District Organization',
    author='Rtr. Neil Trini Lasrado',
    author_email='neil@rotaractsuncity.in',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
