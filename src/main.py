from resp_file_Loader import Loader as FileLoader
from resp_img_Loader import Loader as ImgLoader
from GUI_management_home import GUIHome as GUI
from GUI_management_getSheetData import GUISheetData as GUI2
#from _Loader import Loader
# from from_image.Loader.py import Loader
import tkFileDialog

class Main():

    def __init__(self):
        # Define some nice constants
        self.VERBOSE_OFF = self.CHECKBOX_UNCHECKED = 0
        self.VERBOSE_ON = self.CHECKBOX_CHECKED = 1

        gui = GUI()

        """
        # Load stuff from an image
        imageLoader = ImgLoader()
        imageLoader.load("test3.png")
        imageLoader.save("save_file.dat")
        """

        self.file = open("save_file.dat")
        self.loader = FileLoader(self.file)
        self.loader.parse(self.VERBOSE_OFF)
        for question in self.loader.getSheetByID("00000000").getQuestions(self.VERBOSE_OFF):
            if int(question.getID()) == 2:
                print question.getAnswer()

    def a(self):
        print "a"

    def b(self):
        print "b"

    def c(self):
        print "c"

Main()
