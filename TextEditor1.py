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

#Ember alpha build 1.0
from tkinter import *
from tkinter import ttk
import time as t
from tkinter import filedialog as fd
import os

#Config
User = "TestingUser"
sizeoftext = 15
Theme = "#ff974d"#Dark
Theme2 = "#ffa769"#Light
Font = "Calibri"
TextColour = "Black"
CurrentFile = ""
Status = ""
SKForm = Tk()
SKForm.title('Ember')
Contents = ""
numericaldebounce = 0


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
    filename = os.path.basename(f.name)
    CurrentFile = filename
    Main()
    Title()


def FileFrame():
    FileFrame = Frame(SKForm,width=200,height=244,background=Theme)
    FileFrame.place(x=0,y=85)
    NewFile = Button(FileFrame,width=28,height=2,background=Theme2,text="New File",bd=0,font=(Font,10),fg="White")
    NewFile.place(x=0,y=3)
    Open = Button(FileFrame,width=28,height=2,background=Theme2,text="Open File",bd=0,font=(Font,10),fg="White",command=open_text_file)
    Open.place(x=0,y=43)
    SaveFile = Button(FileFrame,width=28,height=2,background=Theme2,text="Save As",bd=0,font=(Font,10),fg="White")
    SaveFile.place(x=0,y=83)
    Export = Button(FileFrame,width=28,height=2,background=Theme2,text="Export As",bd=0,font=(Font,10),fg="White")
    Export.place(x=0,y=123)
    CloseMenu = Button(FileFrame,width=28,height=2,background=Theme2,text="Close Window",bd=0,font=(Font,10),fg="White",command=FileFrame.destroy)
    CloseMenu.place(x=0,y=163)
    CloseProgram = Button(FileFrame,width=28,height=2,background=Theme2,text="Exit Program",bd=0,font=(Font,10),fg="White",command=SKForm.destroy)
    CloseProgram.place(x=0,y=203)

def EditFrame():
    EditFrame = Frame(SKForm,width=200,height=163,background=Theme)
    EditFrame.place(x=30,y=85)
    EditFormat = Button(EditFrame,width=28,height=2,background=Theme2,text="Edit Format",bd=0,font=(Font,10),fg="White")
    EditFormat.place(x=0,y=3)
    EditName = Button(EditFrame,width=28,height=2,background=Theme2,text="Edit Name",bd=0,font=(Font,10),fg="White")
    EditName.place(x=0,y=43)
    EditPage = Button(EditFrame,width=28,height=2,background=Theme2,text="Edit Page",bd=0,font=(Font,10),fg="White")
    EditPage.place(x=0,y=83)
    CloseMenu = Button(EditFrame,width=28,height=2,background=Theme2,text="Close Window",bd=0,font=(Font,10),fg="White",command=EditFrame.destroy)
    CloseMenu.place(x=0,y=123)


def InsertFrame():
    InsertFrame = Frame(SKForm,width=200,height=163,background=Theme)
    InsertFrame.place(x=70,y=85)
    ImageFile = Button(InsertFrame,width=28,height=2,background=Theme2,text="Insert Image",bd=0,font=(Font,10),fg="White")
    ImageFile.place(x=0,y=3)
    InsertHyper = Button(InsertFrame,width=28,height=2,background=Theme2,text="Insert Hyperlink",bd=0,font=(Font,10),fg="White")
    InsertHyper.place(x=0,y=43)
    InsertTable = Button(InsertFrame,width=28,height=2,background=Theme2,text="Insert Table",bd=0,font=(Font,10),fg="White")
    InsertTable.place(x=0,y=83)
    CloseMenu = Button(InsertFrame,width=28,height=2,background=Theme2,text="Close Window",bd=0,font=(Font,10),fg="White",command=InsertFrame.destroy)
    CloseMenu.place(x=0,y=123)


def EditTextFrame():
    FileFrame = Frame(SKForm,width=200,height=324,background=Theme)
    FileFrame.place(x=150,y=85)
    NewFont = Button(FileFrame,width=28,height=2,background=Theme2,text="Edit Text Font",bd=0,font=(Font,10),fg="White")
    NewFont.place(x=0,y=3)
    EditColour = Button(FileFrame,width=28,height=2,background=Theme2,text="Edit Text Colour",bd=0,font=(Font,10),fg="White")
    EditColour.place(x=0,y=43)
    EditTextSize = Button(FileFrame,width=28,height=2,background=Theme2,text="Edit Text Size",bd=0,font=(Font,10),fg="White")
    EditTextSize.place(x=0,y=83)
    HighlightText = Button(FileFrame,width=28,height=2,background=Theme2,text="Highlight Text",bd=0,font=(Font,10),fg="White")
    HighlightText.place(x=0,y=123)
    Italics = Button(FileFrame,width=28,height=2,background=Theme2,text="Use Italics",bd=0,font=(Font,10),fg="White")
    Italics.place(x=0,y=163)
    Bold = Button(FileFrame,width=28,height=2,background=Theme2,text="Use Bold",bd=0,font=(Font,10),fg="White")
    Bold.place(x=0,y=203)
    Underline = Button(FileFrame,width=28,height=2,background=Theme2,text="Underline Text",bd=0,font=(Font,10),fg="White")
    Underline.place(x=0,y=243)
    CloseMenu = Button(FileFrame,width=28,height=2,background=Theme2,text="Close Window",bd=0,font=(Font,10),fg="White",command=FileFrame.destroy)
    CloseMenu.place(x=0,y=283)

def SettingsFrame():
    EditFrame = Frame(SKForm,width=200,height=163,background=Theme)
    EditFrame.place(x=220,y=85)
    EditFormat = Button(EditFrame,width=28,height=2,background=Theme2,text="Edit Format",bd=0,font=(Font,10),fg="White")
    EditFormat.place(x=0,y=3)
    EditName = Button(EditFrame,width=28,height=2,background=Theme2,text="Edit Name",bd=0,font=(Font,10),fg="White")
    EditName.place(x=0,y=43)
    EditPage = Button(EditFrame,width=28,height=2,background=Theme2,text="Edit Page",bd=0,font=(Font,10),fg="White")
    EditPage.place(x=0,y=83)
    CloseMenu = Button(EditFrame,width=28,height=2,background=Theme2,text="Close Window",bd=0,font=(Font,10),fg="White",command=EditFrame.destroy)
    CloseMenu.place(x=0,y=123)

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
    print(User)
    User = Button(menu,width = 100,height=1,background=Theme,text="Welcome, "+str(User),bd=0,fg="White",font=("Calibri",10),anchor=W,padx=15)
    User.place(x=1355,y=12)

    BETA = Button(SKForm,width = 100,height=1,text="Ember Texteditor Version 2.3.3",bd=0,fg="Orange",font=("Calibri",10),anchor=W,padx=15)
    BETA.place(x=0,y=760)

    File = Button(menu2,width=9,height=2,background=Theme2,bd=0,text="File",fg="White",font=("Calibri",10),command=FileFrame)
    File.place(x=0,y=1)

    Edit = Button(menu2,width=9,height=2,background=Theme2,bd=0,text="Edit",fg="White",font=("Calibri",10),command=EditFrame,anchor=CENTER)
    Edit.place(x=60,y=1)

    Insert = Button(menu2,width=9,height=2,background=Theme2,bd=0,text="Insert",fg="White",font=("Calibri",10),command=InsertFrame,anchor=CENTER)
    Insert.place(x=120,y=1)

    TextS = Button(menu2,width=11,height=2,background=Theme2,bd=0,text="Text Settings",fg="White",font=("Calibri",10),command=EditTextFrame,anchor=CENTER)
    TextS.place(x=190,y=1)

    Settings = Button(menu2,width=9,height=2,background=Theme2,bd=0,text="Settings",fg="White",font=("Calibri",10),command=SettingsFrame,anchor=CENTER)
    Settings.place(x=285,y=1)

    ReportText = Label(menu2,width=9,height=2,background=Theme2,bd=0,text="Size: "+str(sizeoftext),fg="White",font=("Calibri",10),command=ScaleTextDown(),anchor=CENTER)
    ReportText.place(x=530,y=4)

    ReportFont = Label(menu2,width=11,height=2,background=Theme2,bd=0,text="Font: "+str(Font),fg="White",font=("Calibri",10),command=ScaleTextDown(),anchor=CENTER)
    ReportFont.place(x=435,y=4)

    About = Button(menu2,width=9,height=2,background=Theme2,bd=0,text="About",fg="White",font=("Calibri",10),anchor=CENTER)
    About.place(x=355,y=1)

    indent = Frame(width=100000,height=30)
    indent.pack(side=TOP)

    Vsrl.configure(style = 'TScrollbar')
    print(str(Contents))
    MyTkTextBox = Text(SKForm, yscrollcommand = Vsrl.set,font=(Font),fg=TextColour,bd=0)
    MyTkTextBox.config(wrap = NONE, width = 100, height = 100)
    MyTkTextBox.insert(INSERT,str(Contents))
    MyTkTextBox.pack(side = TOP)
    Vsrl.config(command = MyTkTextBox.yview)


Main()
SKForm.mainloop()
