from Tkinter import Label as TLabel
from Tkinter import StringVar

class Label():
    def __init__(self,notself,labels):
        self.textVar = StringVar()
        self.label = TLabel(notself,textvariable=self.textVar)
        self.textVar.set(labels)

    def get(self):
        return self.label

    def set(self,labels):
        self.textVar.set(labels)
