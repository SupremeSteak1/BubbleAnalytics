# Find example dataset in root directory named dataset_1.example
from Sheet import Sheet

class Loader():

    def __init__(self, srcFile):
        self.srcFile = srcFile

    def parse(self):
        # load = self.srcFile.readline()
        sheets = [ ]
        previousSheet = Sheet()
        for load in self.srcFile:
            lst = list(load)
            if lst[0] == '#':
                print "Comment found"
            else:
                print "No comment found; continuing parsing"
                count = 0
                for c in lst:
                    if c == ' ':
                        count += 1
                    else:
                        break
                print "Found " + str(count) + " spaces"
                if count == 0:

            print ""


# The main test area
file = open("test_data.dat")
loader = Loader(file)
loader.parse()
