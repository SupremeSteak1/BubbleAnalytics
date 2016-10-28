from Loader import Loader
#from _Loader import Loader
# from from_image.Loader.py import Loader

# Define some nice constants
VERBOSE_OFF = 0
VERBOSE_ON = 1

# Load stuff from an image
imageLoader = Loader()

# The main test area
file = open("response_loading/src/from_file/test_data.dat")
loader = Loader(file)
loader.parse(VERBOSE_OFF)
loader.getSheetByID("00000001").getQuestions(VERBOSE_OFF)
for question in loader.getSheetByID("00000001").getQuestions(VERBOSE_OFF):
    if int(question.getID()) == 001:
        print question.getAnswer()
