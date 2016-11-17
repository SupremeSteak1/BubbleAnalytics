from Tkinter import Spinbox as Spinnert

class Spinner():
    def __init__(self,notself,_from,_to):
        self.spinner = Spinnert(notself,from_=_from,to=_to)

    def get(self):
        return self.spinner
