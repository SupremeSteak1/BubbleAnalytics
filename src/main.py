from resp_file_Loader import Loader as FileLoader
from resp_img_Loader import Loader as ImgLoader
#from _Loader import Loader
# from from_image.Loader.py import Loader

# Define some nice constants
VERBOSE_OFF = 0
VERBOSE_ON = 1

# Load stuff from an image
#imageLoader = ImgLoader()
#imageLoader.load("test3.png")
#imageLoader.save("save_file.dat")

file = open("save_file.dat")
loader = FileLoader(file)
loader.parse(VERBOSE_ON)
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
