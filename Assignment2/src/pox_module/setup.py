#!/usr/bin/env python
'''Setuptools params'''

from setuptools import setup, find_packages

setup(
    name='cs414',
    version='0.0.0',
    description='Network controller for JHU Computer Networks (CS414), Spring 2021,'
    'adapted from Stanford CS144 course: https://bitbucket.org/huangty/cs144_lab3',
    author='Katarina Mayer (CS414 TA)',
    packages=find_packages(exclude='test'),
    classifiers=[
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Programming Language :: Python",
          "Development Status :: 1 - Planning",
          "Intended Audience :: Developers",
          "Topic :: Internet",
      ],
      license='GPL',
      install_requires=[
        'setuptools',
        'twisted',
        'ltprotocol', # David Underhill's nice Length-Type protocol handler
      ])

