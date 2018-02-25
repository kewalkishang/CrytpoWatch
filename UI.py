import tkinter as tk
from CryptoNotifyer import GetCrytoNames, UpdatePrices
from PIL import Image, ImageTk
root = tk.Tk()
root.title('Crypto Watch')
root.geometry("500x400")
root.resizable(width=False, height=False)

def helloCallBack():
    ans = GetCrytoNames()
    price=UpdatePrices
    #print(price)
    for i in ans:
        label = tk.Label( root, text = "hello", relief=tk.SUNKEN) 
        label.pack() 
        label.config(text)
    
    
   
    
  
  # tkMessageBox.showinfo( "Hello Python", "Hello World") 





B = tk.Button(root,text= "add" , command = helloCallBack)
       
B.pack()


tk.mainloop()