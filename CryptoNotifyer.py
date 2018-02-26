# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 19:28:50 2018

@author: kewal
"""
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
  except:
       #print("Unexpected error:")
       data={'prices':{'BTC': 'ERROR', 'ETH': 'ERROR', 'XRP': 'ERROR', 'BCH': 'ERROR', 'LTC': 'ERROR', 'MIOTA': 'ERROR', 'OMG': 'ERROR', 'ZRX': 'ERROR', 'GNT': 'ERROR', 'REQ': 'ERROR'}}
  finally:
      return data

         
         
            
            



