import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

def ColourChange():
    pass

def FontChange():
    pass

def NewFile():
    pass

def OpenFile():
    pass

def SaveFile():
    pass

def CutText():
    pass

def CopyText():
    pass

def PasteText():
    pass

def AboutSystem():
    pass

def Quit():
    pass

Master = Tk()
Master.title("Ember")
File = None
Master_width = 500
Master_height = 500
screen_width = Master.winfo_screenwidth()
screen_height = Master.winfo_screenheight()
x = int ((screen_width / 2) - (Master_width / 2))
y = int ((screen_height / 2) - (Master_height / 2))
Master.geometry("{}x{}+{}+{}".format(Master_width, Master_height, x, y))
ChosenFont = StringVar(Master)
ChosenFont.set("Arial")
ChosenSize = StringVar(Master)
ChosenSize.set("25")
TextContainer = Text(Master, font=(ChosenFont.get(), ChosenSize.get()))
Scroll = Scrollbar(TextContainer)
Master.grid_rowconfigure(0,weight=1)
Master.grid_columnconfigure(0,weight=1)
TextContainer.grid(sticky=N +E + S+ W)
Frame = Frame(Master)
Frame.grid(sticky=W)
MenuLabel = Menu(Master)
Master.config(menu=MenuLabel)
File = Menu(MenuLabel, tearoff=0)
MenuLabel.add_cascade(label="file",menu=File,activebackground="#ff9152")
File.add_command(label="File",menu=None)

ColourChange = Button(Frame, text="Colour",command=ColourChange)
ColourChange.grid(row=0,column=0)

Scroll.pack(side=RIGHT,fill=Y)
TextContainer.config(yscrollcommand=Scroll.set)




Master.mainloop()
