# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 21:25:21 2018

@author: kewal
"""
from tkinter import *
import tkinter.messagebox
root=Tk()

#FRAMES 
'''topframe=Frame(root)
topframe.pack()
bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM)
but1=Button(bottomframe,text="submit 1",fg='black')
but1.pack(side=LEFT)
but2=Button(bottomframe,text="submit 2 ",fg='black')
but2.pack(side=LEFT)
but3=Button(bottomframe,text="submit 3",fg='black')
but3.pack(side=LEFT)'''

#DYNAMIC LAYOUT
'''lab1= Label(root,text="one1",bg='red')
lab1.pack()     
lab1= Label(root,text="one2",bg='green')
lab1.pack(fill=X)         
lab1= Label(root,text="one1",bg='blue')
lab1.pack(side=LEFT,fill=Y)      '''
         
#GRID
'''lab1=Label(root,text="Name")
lab2= Label(root,text="password")
entry1=Entry(root)
entry2=Entry(root)
lab1.grid(row=0,column=0 ,sticky=W)
lab2.grid(row=1,column=0,sticky=W)
entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)
c= Checkbutton(root,text="keep me logged in")
c.grid(columnspan=2)'''

#binding a function to layouts
'''def printName(event):
    print("kewal")
but1=Button(root,text="print", fg='black')
but1.bind("<Button-1>",printName)
but1.pack()'''
#mouse click events
'''def left(event):
    print("left")
def right(event):
    print("right")
def middle(event):
    print("middle")

frame=Frame(root,width=300,height=250)
frame.bind("<Button-1>",left)
frame.bind("<Button-2>",middle)
frame.bind("<Button-3>",right)
frame.pack()'''

#CLASSES
'''class Buttons:
    def __init__(self,master):
        frame=Frame(master)
        frame.pack()
        
        self.but1=Button(frame,text="print",command=self.printMsg)
        self.but1.pack(side=LEFT)
        
        self.quit=Button(frame,text="QUIT",command=frame.quit)
        self.quit.pack(side=LEFT)
        
    def printMsg(self):
        print("wow this worked")
b=Buttons(root)'''

#spinbox

def get_va():
    print(sb.get())
var = StringVar()
sb = Spinbox(root, values=("f","u","r"), textvariable=var, width=10)
sb.pack()
but1=Button(root,text='get',command=get_va)
but1.pack()

#DROP DOWN MENU
'''def DoNothing():
    print("i wont")
menu =Menu(root)
root.config(menu=menu)
submenu=Menu(menu)
menu.add_cascade(label='file',menu=submenu)
submenu.add_command(label="new poject",command=DoNothing)
submenu.add_command(label="new poject2",command=DoNothing)
submenu.add_command(label="new poject3",command=DoNothing)
submenu.add_separator()
submenu.add_command(label="exit",command=DoNothing)
editmenu=Menu(menu)
menu.add_cascade(label='edit',menu=editmenu)
editmenu.add_command(label="redo",command=DoNothing)'''

#toolbar
'''toolbar=Frame(root,bg='blue')
but1=Button(toolbar,text='insert Image')
but1.pack(side=LEFT, padx=2,pady=2)
but1=Button(toolbar,text='Print')
but1.pack(side=LEFT, padx=2,pady=2)

toolbar.pack(side=TOP,fill=X)    '''

#status bar
'''status=Label(root,text="do nothign bro",bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM,fill=X)'''
               
#MESSAGEBOX
'''tkinter.messagebox.showinfo("window title","bro,do you even lift?")
answer= tkinter.messagebox.askquestion("uestion 1?","do you like GOT")
if answer == 'yes':
    print("awesome")'''

#shapes and grahics
'''canvas=Canvas(root,width=200,height=100)
canvas.pack()
blackline=canvas.create_line(0,0,200,50)
redline=canvas.create_line(0,100,200,50,fill="red")
greenBox=canvas.create_rectangle(25,25,130,60,fill="green")
canvas.delete(redline)    '''

#Images and Icons
'''photo=PhotoImage(file="add.png")
label=Label(root,image=photo)
label.pack()  

           
root.mainloop()'''

#OPEN A NEW WINDOW             
'''import tkinter as tk
i =0
def create_window():
    window = tk.Toplevel(root)
    
    label.config(text="this is bs")

root = tk.Tk()
label=tk.Label(root, text=i )
label.pack()
b = tk.Button(root, text="Create new window", command=create_window)
b.pack()'''

root.mainloop()

#checkbox 
'''from tkinter import *
master = Tk()

def var_states():
   print("male: %d,\nfemale: %d" % (var1.get(), var2.get()))

Label(master, text="Your sex:").grid(row=0, sticky=W)
var1 = IntVar()
Checkbutton(master, text="male", variable=var1).grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(master, text="female", variable=var2).grid(row=2, sticky=W)
Button(master, text='Quit', command=master.quit).grid(row=3, sticky=W, pady=4)
Button(master, text='Show', command=var_states).grid(row=4, sticky=W, pady=4)
mainloop()'''

#!/usr/bin/python3
'''from tkinter import *
class Checkbar(Frame):
   def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
      Frame.__init__(self, parent)
      self.vars = []
      for pick in picks:
         var = IntVar()
         chk = Checkbutton(self, text=pick, variable=var)
         chk.pack(side=side, anchor=anchor, expand=YES)
         self.vars.append(var)
   def state(self):
      return map((lambda var: var.get()), self.vars)
if __name__ == '__main__':
   root = Tk()
   lng = Checkbar(root, ['Python', 'Ruby', 'Perl', 'C++'])
  # tgl = Checkbar(root, ['English','German'])
   lng.pack(side=TOP,  fill=X)
  # tgl.pack(side=LEFT)
   lng.config(relief=GROOVE, bd=2)

   def allstates(): 
      print(list(lng.state()))
  # Button(root, text='Quit', command=root.quit).pack(side=RIGHT)
   Button(root, text='Peek', command=allstates).pack(side=RIGHT)
   root.mainloop()'''