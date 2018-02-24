# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 19:28:50 2018

@author: kewal
"""
import numpy as np
import urllib.request, json 
import threading
from datetime import datetime
'''print("Enter your name")
INP = input()
#print(INP)
print("hello", INP ,"first part is done")
input("Press Enter to continue...")'''


def UpdatePrices():
  try:  
     with urllib.request.urlopen("https://koinex.in/api/ticker") as url:
        data = json.loads(url.read().decode())
        print(str(datetime.now()),data['prices']['XRP'])
        threading.Timer(10, UpdatePrices).start()
  except:
       print("Unexpected error:")
       threading.Timer(20, UpdatePrices).start()
      
       
UpdatePrices()





