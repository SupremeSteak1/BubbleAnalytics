# Find example dataset in root directory named dataset_1.example
from Sheet import Sheet
from Question import Question

class Loader():

    def __init__(self, srcFile):
        self.srcFile = srcFile

    def parse(self):
        # load = self.srcFile.readline()
        sheets = [ ]
        previousSheet = Sheet("00000000")
        previousQuestion = Question("000")
        for line in self.srcFile:
            lst = list(line)
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
                    # This is a sheet id number (universally)
                    previousSheet = Sheet(''.join(lst))
                    print "Created a new sheet element with id: " + str(line)
                elif count == 1:
                    # This is a unique question id (with respect to the sheet id)
                    del lst[0]
                    previousQuestion = Question(''.join(lst))
                    previousSheet.addQuestion(previousQuestion)
                    print "Created a new question with id: " + ''.join(lst)
                elif count == 2:
                    # This is either a question type or question answer. Answers will have a '[' in front of them.
                    if lst[2] == '[':
                        del lst[0:3]
                        previousQuestion.setAnswer(''.join(lst))
                        print "Added answer " + ''.join(lst)
                    else:
                        del lst[0:2]
                        previousQuestion.setType(''.join(lst))
                        print "Added type " + ''.join(lst)
                    previousSheet.setQuestion(previousQuestion.getID,previousQuestion)
                    print "Updated question"
            print ""


# The main test area
file = open("test_data.dat")
loader = Loader(file)
loader.parse()
