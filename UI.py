from CryptoNotifyer import GetCrytoNames,UpdatePrices
import tkinter as tk 
import tkinter.messagebox
import threading
root = tk.Tk()
root.title("Crypto Watch")
#root.geometry("200x300")
root.minsize(100,100)
root.resizable(width=False, height=False)
va=[]
labels = []

window=[]
one=[]
sign=[]
threshold=[]
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
        c=tk.Checkbutton(window, text=i, variable=var1).pack(anchor=tk.W)
        va.append(var1)
    b = tk.Button(window,text="GO",command=getva)
    b.pack()
    window.protocol("WM_DELETE_WINDOW", quit_win) 

def getva():
     
       for a in va:           
           if a.get()==1:               
               i=0              
               for lab in labels:
                   lab.destroy()
               
               for ent in threshold:
                   ent.destroy()
               
               for si in sign:
                   si.destroy()
               #print(len(labels))
               labels.clear()
               one.clear()
               threshold.clear()
               sign.clear()
               ro=0
               for a in va:
                   
                   if a.get()==1:
                      
                       one.append(i)
                       label1=tk.Label(topframe,text=crp[i] )
                       label1.grid(row=ro,column=0,sticky=tk.W)
                       var = tk.StringVar()
                       sb = tk.Spinbox(topframe, values=("~","<",">"), textvariable=var, width=3)
                       sb.grid(row=ro,column=1)
                       E1 = tk.Entry(topframe)                
                       E1.config(width=6)                       
                       E1.grid(row=ro,column=2)
                       labels.append(label1)
                      
                       sign.append(sb)
                       threshold.append(E1)
                       ro+=1
                   i+=1  
                 
               RefreshLabel()
               return
       for si in sign:
                   si.destroy()
       for lab in labels:
                   lab.destroy()
       for ent in threshold:
                   ent.destroy()
  
       one.clear()
       sign.clear()
       threshold.clear()
       labels.clear()            
       label1=tk.Label(topframe,text="Click on + to add cryptos")
       label1.pack()
       labels.append(label1)
          

topframe=tk.Frame(root,width=200,height=250)
topframe.pack()
bottomframe=tk.Frame(root)
bottomframe.pack(side=tk.BOTTOM)

def notification(data):
  
    for i in range(len(threshold)):
        th=0
        if not threshold[i].get():
            th=0
        else:
            th=threshold[i].get()
        si=sign[i].get()
        #print(th)
        if data['prices'][crp[one[i]]] !="ERROR":
            if si=="<" and float(data['prices'][crp[one[i]]])<float(th):
               tkinter.messagebox.showwarning("FALL UPDATE", crp[one[i]]+" is lesser than "+th)
            elif si==">" and float(data['prices'][crp[one[i]]])>float(th):
                 tkinter.messagebox.showwarning("RISE UPDATE", crp[one[i]]+" is greater than "+th)
            
   
def RefreshLabel():
     
      data=UpdatePrices()
    
      #print(data['prices'])
      d=0
      for lab in labels:
          lab.config(text=crp[one[d]]+"  -  "+str(data['prices'][crp[one[d]]]))
          d+=1
      notification(data)   
      global t
      t=threading.Timer(20, RefreshLabel)
      t.start()
      
label=tk.Label(topframe, text="Click on + to add cryptos" )
label.pack()
labels.append(label)
but = tk.Button(bottomframe,text="[+]",command=neww)
but.pack()


def quit_root():
    t.cancel()
    root.destroy()
    #print("root")
root.protocol("WM_DELETE_WINDOW", quit_root) 



root.mainloop()