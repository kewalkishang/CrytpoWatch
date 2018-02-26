from CryptoNotifyer import GetCrytoNames
import tkinter as tk  
root = tk.Tk()
root.title("Crypto Watch")
root.geometry("300x300")
root.resizable(width=False, height=False)
va=[]
labels = []
window=[]
crp=GetCrytoNames()
def neww():
    def quit_win():
        window.destroy()
        but.config(state=tk.ACTIVE)
    window=tk.Toplevel()
    but.config(state=tk.DISABLED)
    window.resizable(width=False, height=False)
    va.clear()
    for i in crp:
        var1 = tk.IntVar()
        c=tk.Checkbutton(window, text=i, variable=var1).pack()
        va.append(var1)
    b = tk.Button(window,text="get",command=getva)
    b.pack()
    window.protocol("WM_DELETE_WINDOW", quit_win) 

def getva():
      
       for a in va:
           if a.get()==1:
        
               i=0
               for lab in labels:
                   lab.destroy()
               print(len(labels))
               labels.clear()
               for a in va:
                   
                   if a.get()==1:
                       label1=tk.Label(topframe,text=crp[i] )
                       label1.pack()
                       labels.append(label1)
                   i+=1          
               return
       for lab in labels:
                   lab.destroy()
       labels.clear()            
       label1=tk.Label(topframe,text="Click on + to add cryptos")
       label1.pack()
       labels.append(label1)
          

topframe=tk.Frame(root,width=200,height=250)
topframe.pack()
bottomframe=tk.Frame(root)
bottomframe.pack(side=tk.BOTTOM)

label=tk.Label(topframe, text="Click on + to add cryptos" )
label.pack()
labels.append(label)
but = tk.Button(bottomframe,text="Update",command=neww)
but.pack()






root.mainloop()