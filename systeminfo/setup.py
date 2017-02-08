'''
Created on 8 Feb 2017

@author: thomasflood
'''
from setuptools import setup

setup(name="systeminfo",
      version="0.1",
      description="Basic system information for comp30670",
      url="",
      author="Thomas Flood",
      author_email="thomaspeterflood@gmail.com",
      licence="GPL3",
      packages=['systeminfo'],
      entry_points={
          'console_scripts':['comp30670_systeminfo=systeminfo.main:main'],
          }
      )