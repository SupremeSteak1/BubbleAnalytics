from Tkinter import *
import tkFileDialog
from GUI_element_Checkbox import Checkbox as Checkbox
from GUI_element_button import Button as Buttonb
from GUI_element_label import Label as Label
from GUI_element_spinner import Spinner as Spinnerb

class MainWindowManager(Frame):
    def __init__(self, parent):
        Frame.__init__(self,parent,background="white")
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Main Menu")
        self.pack(fill=BOTH, expand=True)
        self.var = BooleanVar()

    def addCheckbox(self,text,xc,yc,toggled,function):
        cb = Checkbox(self,text,function)
        if toggled:
            cb.get().select()
        cb.get().place(x=xc,y=yc)
        return cb

    def addButton(self,label,xc,yc,state,function):
        bt = Buttonb(self,label,state,function)
        bt.get().place(x=xc,y=yc)
        return bt

    def addLabel(self,label,xc,yc):
        lb = Label(self,label)
        lb.get().place(x=xc,y=yc)
        return lb

    def addSpinner(self,_from,_to,xc,yc):
        sp = Spinnerb(self,_from,_to)
        sp.get().place(x=xc,y=yc)
        return sp

    def onClick(self):
        if self.var.get() == True:
            print "Button pressed"
        else:
            print "Button depressed"
