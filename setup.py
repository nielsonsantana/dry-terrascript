import os
import re

from setuptools import setup


def read_file(*paths):
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, *paths)
    return open(path).read() if os.path.exists(path) else ''


def get_version():
    return read_file('VERSION')


# Get long_description from README.md:
long_description = read_file('README.md')
long_description = long_description.split('<!---split here-->', 1)[0]

setup(
    name='dry_terrascript',
    version=get_version(),
    description="Set of code to prevent repeat code",
    long_description=long_description,
    include_package_data=True,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='terraform terrascript python',
    author='Nielson Santana',
    author_email='nielsonnas@gmail.com',
    maintainer='',
    license='MIT',
    packages=['dry_terrascript'],
    zip_safe=False,
)
