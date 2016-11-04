from Tkinter import Tk, Frame, Checkbutton, BooleanVar, BOTH

class Button():
    def __init__(self,notself,label):
        self.var = BooleanVar()
        self.button = Checkbutton(notself,text=label, variable=self.var, command=self.onClick)

    def get(self):
        return self.button

    def onClick(self):
        if self.var.get() == True:
            print "Button pressed"
        else:
            print "Button depressed"
