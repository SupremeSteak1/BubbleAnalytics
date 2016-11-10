from Tkinter import Tk, Frame, Checkbutton, BooleanVar, BOTH

class Checkbox():
    def __init__(self,notself,label,function):
        self.var = BooleanVar()
        self.cb = Checkbutton(notself,text=label, variable=self.var, command=function)

    def get(self):
        return self.cb
