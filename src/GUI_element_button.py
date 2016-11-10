from Tkinter import Button as Buttont

class Button():
    def __init__(self,notself,label,state,function):
        self.button = Buttont(notself,text="Test",state=state,command=function)

    def get(self):
        return self.button
