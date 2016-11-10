from Tkinter import Button as Buttont

class Button():
    def __init__(self,notself,label,function):
        self.button = Buttont(notself,text="Test",command=function)

    def get(self):
        return self.button
