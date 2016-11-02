from Tkinter import Tk, Frame, Checkbutton, BooleanVar, BOTH
from GUI_element_Checkbox import Checkbox as Checkbox

class WindowManager(Frame):
    def __init__(self, parent):
        Frame.__init__(self,parent,background="white")
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Main Menu")
        self.pack(fill=BOTH, expand=True)
        self.var = BooleanVar()

        addCheckbox("This is the 2nd box",10,10)

        cb = Checkbutton(self, text="This is a checkbox", variable=self.var, command=self.onClick)
        cb.select()
        cb.place(x=50,y=50)

    def addCheckbox(self,text,xc,yc):
        cb = Checkbox(self,text)
        cb.get().place(x=xc,y=yc)

    def onClick(self):
        if self.var.get() == True:
            print "Button pressed"
        else:
            print "Button depressed"
