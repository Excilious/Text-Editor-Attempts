from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog as fd
import os

Main = Tk()
Main.title("Ember")

class Ember:
    def __init__(self,ttkMain):
        #Setting up values :)
        self.User = "BetaUser"
        self.CurrentFile = None
        self.CurrentContents = None
        self.Theme = "Original"
        self.DictThemes = {
            "Original":["#ff9152","#ff9152"]
        }
        self.Position = 20
        self.FileQueue = []
        self.Main = ttkMain

    def OpenFiles(self):
        filetypes = (('Text Files', '*.txt'), ('All Files', '*.*'))
        file = fd.askopenfile(filetypes=filetypes)
        if file == None: return
        self.CurrentContents = file.readlines()
        self.CurrentFile = os.path.basename(str(file.name)).split('/')[-1]
        self.TabManager()
        #We have the contents of the file, now we need to display it.

    def Tabs(self,Name=None):
        TabFrame = Frame(self.Main,width=2000,height=33,bg=self.DictThemes[self.Theme][1])
        TabFrame.place(x=0,y=39)
        PageFrame = Frame(self.Main,width=900,height=2000,bg="White")
        PageFrame.place(x=275,y=90)

    def ControlMenu(self):
        Base = Frame(self.Main,width=20000,height=37,bg=self.DictThemes[self.Theme][0])
        Base.place(x=0,y=0)
        File = Button(
            self.Main,width=100,height=2,
        background=self.DictThemes[self.Theme],
        text="File",bd=0,fg="White",font=("Calibri",10),
        anchor=W,padx=15,activeforeground="White",
        activebackground=self.DictThemes[self.Theme][0],
        relief=RIDGE,command=self.OpenFiles)
        File.place(x=0,y=0)

    def UpdateScrollbar(self):
        Scrollframe = Frame(self.Main,width=4,height=50,bg=self.DictThemes[self.Theme][0])
        Scrollframe.place(x=1160,y=100)

    def ChangePage(self):
        #messagebox.askyesno("Save File?","Do you want to save "+str(self.CurrentFile)+"?")
        TextBox = Text(self.Main,width=100,height=43,bd=0,bg="White")
        TextBox.place(x=320,y=105)
        TextBox.insert(END,self.CurrentContents)
        self.UpdateScrollbar()

    def TabManager(self):
        SelectedWidth = 12
        if self.CurrentFile not in self.FileQueue:
            DefaultBase = Button(
                self.Main,width = SelectedWidth, 
            height=1,background="White",
            text=self.CurrentFile,bd=0,
            fg=self.DictThemes[self.Theme],
            font=("Calibri",10),
            activeforeground=self.DictThemes[self.Theme][0],
            activebackground="White",
            relief=RIDGE,
            command=self.ChangePage()
            )
            DefaultBase.place(x=self.Position,y=43)
            self.Position += 95
            self.FileQueue.append(self.CurrentFile)

Runtime = Ember(Main)
Runtime.Tabs()
Runtime.ControlMenu()
Main.mainloop()
