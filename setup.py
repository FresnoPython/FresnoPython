#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name='FresnoPython',
    version='1.0.0',
    author='Derek Payton',
    author_email='derek.payton@gmail.com',
    description='Information for the Fresno Python User Group',
    keywords='fresno user group',
    license='MIT',
    url='https://github.com/dmpayton/FresnoPython',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    scripts=['bin/fresno.py'],
    packages=find_packages(exclude=['tests']),
    install_requires=['python-dateutil==2.5.3'],
)
