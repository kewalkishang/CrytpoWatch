# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 19:28:50 2018

@author: kewal
"""

#!pip install cx_Freeze

import cx_Freeze
from cx_Freeze import *

setup(name="CrytoWatch",
      version="0.1",
      description='Crypto Notifyer',
      executables=[Executable("CryptoNotifyer.py")])