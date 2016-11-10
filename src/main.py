from resp_file_Loader import Loader as FileLoader
from resp_img_Loader import Loader as ImgLoader
from WindowManager import WindowManager as GUI
#from _Loader import Loader
# from from_image.Loader.py import Loader
from Tkinter import Tk, Frame, Checkbutton, BooleanVar, BOTH

# Define some nice constants
VERBOSE_OFF = CHECKBOX_UNCHECKED = 0
VERBOSE_ON = CHECKBOX_CHECKED = 1
BUTTON_ENABLED = "active"
BUTTON_DISABLED = "disabled"

def a():
    print "a"

def b():
    print "b"

def c():
    print "c"

# Tkinter stuff
root = Tk()
root.geometry("450x350+300+300")
window = GUI(root)
window.addCheckbox("This is the 1st box",10,10,CHECKBOX_CHECKED,a)
window.addCheckbox("This is the 2nd box",10,40,CHECKBOX_UNCHECKED,b)
window.addCheckbox("This is the 3rd box",10,70,CHECKBOX_CHECKED,a)
window.addCheckbox("This is the 4th box",10,100,CHECKBOX_UNCHECKED,b)
window.addButton("Test button 1",10,130,BUTTON_DISABLED,c)
window.addButton("Open a file",10,160,BUTTON_ENABLED,window.askOpenFile)
root.mainloop()

"""
# Load stuff from an image
imageLoader = ImgLoader()
imageLoader.load("test3.png")
imageLoader.save("save_file.dat")
"""

file = open("save_file.dat")
loader = FileLoader(file)
loader.parse(VERBOSE_OFF)
for question in loader.getSheetByID("00000000").getQuestions(VERBOSE_OFF):
    if int(question.getID()) == 2:
        print question.getAnswer()


# The main test area
#file = open("test_data.dat")
#loader = Loader(file)
#loader.parse(VERBOSE_OFF)
#loader.getSheetByID("00000001").getQuestions(VERBOSE_OFF)
#for question in loader.getSheetByID("00000001").getQuestions(VERBOSE_OFF):
#    if int(question.getID()) == 001:
#        print question.getAnswer()
