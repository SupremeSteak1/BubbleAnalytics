from Tkinter import Tk, Frame, Checkbutton, BooleanVar, BOTH
from MainWindowManager import MainWindowManager as GUI
from resp_file_Loader import Loader as FileLoader
import tkFileDialog
import time

class GUIHome:

    def __init__(self):
        # Define some nice constants
        self.VERBOSE_OFF = self.CHECKBOX_UNCHECKED = 0
        self.VERBOSE_ON = self.CHECKBOX_CHECKED = 1

        self.BUTTON_ENABLED = "active"
        self.BUTTON_DISABLED = "disabled"

        # Tkinter stuff
        self.root = Tk()
        self.root.geometry("850x350+300+300")
        self.window = GUI(self.root)

        self.window.addLabel("Find sheetID:",10,130)
        self.sid = self.window.addSpinner(0,10,10,160)
        self.window.addLabel("Find questionID:",10,190)
        self.qid = self.window.addSpinner(0,10,10,220)

        # Define options for opening or saving a file... because I'm making the assumption the user will open a file
        self.file_opt = self.options = {}
        self.options['defaultextension'] = '.dat'
        self.options['filetypes'] = [('data files', '.dat'), ('all files', '.*')]
        self.options['initialdir'] = ''
        self.options['initialfile'] = '*.dat'
        self.options['parent'] = self.window
        self.options['title'] = 'EXAMPLE TITLE!! REPLACE SOON (OR LATER)'


        self.window.addCheckbox("This is the 1st box",10,10,self.CHECKBOX_CHECKED,self.a)
        self.window.addCheckbox("This is the 2nd box",10,40,self.CHECKBOX_UNCHECKED,self.b)
        self.window.addCheckbox("This is the 3rd box",10,70,self.CHECKBOX_CHECKED,self.a)
        self.window.addCheckbox("This is the 4th box",10,100,self.CHECKBOX_UNCHECKED,self.b)

        self.window.addButton("Load data from a file",10,250,self.BUTTON_ENABLED,self.askOpenFile)
        self.window.addButton("Hide window (hopefully)",10,280,self.BUTTON_ENABLED,self.hideWindow)
        self.root.mainloop()

    def a(self):
        print "a"

    def b(self):
        print "b"

    def hideWindow(self):
        self.root.withdraw()
        time.sleep(2)
        self.showWindow()

    def showWindow(self):
        self.root.update()
        self.root.deiconify()

    def askOpenFile(self):
        try:
            # This is the data file
            df = tkFileDialog.askopenfile(mode='r', **self.file_opt)
            loader = FileLoader(df)
            loader.parse(self.VERBOSE_OFF)
            for question in loader.getSheetByID(self.sid.get().get()).getQuestions(self.VERBOSE_OFF):
                if int(question.getID()) == int(self.qid.get().get()):
                    print "Answer to sheetID " + str(self.sid.get().get()) + ", questionID " + str(self.qid.get().get()) + " is " + str(question.getAnswer())
        except:
            print "Failure loading, parsing or reading information at main.py ~ lines 61-67"
