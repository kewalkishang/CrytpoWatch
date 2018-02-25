# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 19:28:50 2018

@author: kewal
"""
import numpy as np
import urllib.request, json 
import threading
from datetime import datetime
import tkinter as tk
from PIL import Image, ImageTk
root = tk.Tk()
root.title('Crypto Watch')
root.geometry("500x400")
root.resizable(width=False, height=False)
'''print("Enter your name")
INP = input()
#print(INP)
print("hello", INP ,"first part is done")
input("Press Enter to continue...")'''
gok=tk.StringVar()
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

#GetCrytoNames() 

def SetLabels():
    ans = GetCrytoNames()   
    for i in ans:
            label= tk.Label( root, textvariable=gok, relief=tk.SUNKEN) 
            
            label.pack()
            gok.set("hello") 
           
         
         
            
            
    #UpdatePrices()
    
   
        
#UpdatePrices()

label = tk.Label( root, text = "hello", relief=tk.SUNKEN) 
label.pack() 
B = tk.Button(root,text= "add" , command = SetLabels)
       
B.pack()

tk.mainloop()




