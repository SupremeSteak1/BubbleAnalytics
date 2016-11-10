from Tkinter import *
import tkFileDialog
from GUI_element_Checkbox import Checkbox as Checkbox
from GUI_element_button import Button as Buttonb

class WindowManager(Frame):
    def __init__(self, parent):
        Frame.__init__(self,parent,background="white")
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Main Menu")
        self.pack(fill=BOTH, expand=True)
        self.var = BooleanVar()

        # Define options for opening or saving a file... because I'm making the assumption the user will open a file
        self.file_opt = options = {}
        options['defaultextension'] = '.dat'
        options['filetypes'] = [('all files', '.*'), ('text files', '.txt'), ('data files', '.dat')]
        options['initialdir'] = 'C:\\'
        options['initialfile'] = 'unspecified.txt'
        options['parent'] = self
        options['title'] = 'EXAMPLE TITLE!! REPLACE SOON (OR LATER)'

        # Defining options for opening a directory
        self.dir_opt = options = {}
        options['initialdir'] = 'C:\\'
        options['mustexist'] = False
        options['parent'] = self
        options['title'] = 'ALSO REPLACE THIS TEMP TITLE!! IT TOO IS A BAD EXAMPLE'

    def askOpenFile(self):
        # Returns an opened file in read mode.
        return tkFileDialog.askopenfile(mode='r', **self.file_opt)

    def askSaveAsFile(self):
        # Returns an opened file in write mode.
        return tkFileDialog.asksaveasfile(mode='w', **self.file_opt)

    def askDirectory(self):
        # Returns a selected directoryname.
        return tkFileDialog.askdirectory(**self.dir_opt)

    def addCheckbox(self,text,xc,yc,toggled,function):
        cb = Checkbox(self,text,function)
        if toggled:
            cb.get().select()
        cb.get().place(x=xc,y=yc)

    def addButton(self,label,xc,yc,state,function):
        bt = Buttonb(self,label,state,function)
        bt.get().place(x=xc,y=yc)

    def onClick(self):
        if self.var.get() == True:
            print "Button pressed"
        else:
            print "Button depressed"
