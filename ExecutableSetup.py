# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 19:28:50 2018

@author: kewal
"""

#!pip install cx_Freeze

import cx_Freeze
from cx_Freeze import *
import os
includes      = []
include_files = [r"C:\Python34\DLLs\tcl86t.dll", \
                 r"C:\Python34\DLLs\tk86t.dll"]
base = None
if sys.platform == "win32":
    base = "Win32GUI"
    
os.environ['TCL_LIBRARY'] = r"C:\Python34\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Python34\tcl\tk8.6"
setup(name="CrytoWatcha",
      version="0.2",
      description='Crypto Notifyers',
      options = {"build_exe": {"includes": includes, "include_files": include_files}},
      executables=[Executable("UI.py",base=base)])