from Tkinter import Tk, Frame, Checkbutton, BooleanVar, BOTH

class Checkbox():
    def __init__(self,notself,label):
        self.var = BooleanVar()
        self.cb = Checkbutton(notself,text=label, variable=self.var, command=self.onClick)

    def initUI(self):
        self.parent.title("Main Menu")
        self.pack(fill=BOTH, expand=True)
        self.var = BooleanVar()

        self.cb = Checkbutton(self, text="This is a checkbox", variable=self.var, command=self.onClick)
        cb.select()
        cb.place(x=50,y=50)

    def get(self):
        return self.cb

    def onClick(self):
        if self.var.get() == True:
            print "Button pressed"
        else:
            print "Button depressed"
