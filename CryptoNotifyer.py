# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 19:28:50 2018

@author: kewal
"""
import numpy as np
import urllib.request, json 
import threading
from datetime import datetime

def GetCrytoNames():
     CryptoNames=[]
     with urllib.request.urlopen("https://koinex.in/api/ticker") as url:
        data = json.loads(url.read().decode())
        for name in data['prices']:
            CryptoNames.append(name)
        return CryptoNames

def UpdatePrices():
  try:  
     with urllib.request.urlopen("https://koinex.in/api/ticker") as url:
        data = json.loads(url.read().decode())
        #for i in data['prices']:
         #   label.config(text=str(i)+data['prices'][i])
       # gok.set(data["prices"])
        print(str(datetime.now()),data['prices']['XRP'])
        threading.Timer(10, UpdatePrices).start()
  except:
       print("Unexpected error:")
       threading.Timer(20, UpdatePrices).start()

         
         
            
            



