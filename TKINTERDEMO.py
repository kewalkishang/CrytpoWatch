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
photo=PhotoImage(file="add.png")
label=Label(root,image=photo)
label.pack()             
root.mainloop()