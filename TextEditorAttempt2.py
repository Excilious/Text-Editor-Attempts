"""
Copyright (C) 2021-2022 Excilious

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

#---Imports---#
from tkinter import *
from tkinter import ttk
import time as t
from tkinter import filedialog as fd
import os

User = "TestingUser"
sizeoftext = 15
Theme = "#ffa769"#Dark
Theme2 = "#ffa769"#Light
Font = "Calibri"
TextColour = "Black"
CurrentFile = ""
Status = ""
Contents = ""
SKForm = Tk()
SKForm.title('Ember')

def ScaleTextUp():
    global sizeoftext
    sizeoftext += 1
    

def ScaleTextDown():
    global sizeoftext
    sizeoftext = sizeoftext - 1

menu = Frame(width=100000,height=45,background=Theme,bd=0)
menu.pack(side=TOP)
menu2 = Frame(width=100000,height=40,background=Theme2,bd=0)
menu2.pack(side=TOP)

    
Vsrl = ttk.Scrollbar(SKForm)
Vsrl.pack(side = RIGHT, fill = Y)

style = ttk.Style()
style.configure('TScrollbar', background='#2b2b2b', troughcolor='#E0F5DA', arrowcolor='#65E6A9', highlightcolor='#E0F5DA')

def open_text_file():
    global CurrentFile
    global Contents
    filetypes = (('Text Files', '*.txt'), ('All Files', '*.*'))
    f = fd.askopenfile(filetypes=filetypes)
    print(f.readlines())
    Contents = f.readlines()
    print(Contents)
    filename = os.path.basename(f.name)
    CurrentFile = filename
    Title()

def Title():
    frm = Label(menu,width = 100,height=1,background=Theme,text=CurrentFile,bd=0,fg="White",font=("Calibri",16),anchor=W,padx=15)
    frm.place(x=0,y=8)
def Main():
    global Theme
    global Theme2
    global CurrentFile
    global User
    global Status
    global Contents

    User = Button(menu,width = 100,height=1,background=Theme,text="Welcome, "+User,bd=0,fg="White",font=("Calibri",10),anchor=W,padx=15)
    User.place(x=1355,y=12)

    BETA = Button(SKForm,width = 100,height=1,text="Ember Texteditor Version 2.3.3",bd=0,fg="Orange",font=("Calibri",10),anchor=W,padx=15)
    BETA.place(x=0,y=760)

    File = Button(menu2,width=9,height=2,background=Theme2,bd=0,text="File",fg="White",font=("Calibri",10),command=open_text_file)
    File.place(x=0,y=1)

    indent = Frame(width=100000,height=30)
    indent.pack(side=TOP)

    Vsrl.configure(style = 'TScrollbar')

    MyTkTextBox = Text(SKForm, yscrollcommand = Vsrl.set,font=(Font),fg=TextColour,bd=0)

    MyTkTextBox.config(wrap = NONE, width = 100, height = 100)
    for i in range(len(Contents)):
        print(str(Contents))
        MyTkTextBox.insert(INSERT,str(Contents))

    MyTkTextBox.pack(side = TOP)

    Vsrl.config(command = MyTkTextBox.yview)
Main()
SKForm.mainloop()
