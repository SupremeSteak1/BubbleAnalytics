# Find example dataset in root directory named dataset_1.example
from Sheet import Sheet
from Question import Question

# Define some nice constants
VERBOSE_OFF = 0
VERBOSE_ON = 1

class Loader():

    def __init__(self, srcFile):
        self.srcFile = srcFile
        self.sheets = [ ]

    def parse(self, verbose):
        # load = self.srcFile.readline()
        previousSheet = Sheet("00000000") # Create some temp variables until proper checking can be put into place
        previousQuestion = Question("000")
        for line in self.srcFile: # Loop through all the lines in the file
            lst = list(line)
            if lst[0] == '#':
                if verbose == VERBOSE_ON:
                    print "Comment found" # Check if the line is a comment
            else: # If not, continue working on it
                count = 0 # Create a variable to store the indent level
                for c in lst:
                    if c == ' ':
                        count += 1 # Add to the indent level
                    else:
                        break
                if verbose == 1:
                    print "Found " + str(count) + " spaces"
                if count == 0:
                    # This is a sheet id number (universally)
                    if len(previousSheet.getQuestions(verbose)) != 0:
                        self.sheets.append(previousSheet)
                        if verbose == 1:
                            print "Appending previous sheet"
                    previousSheet = Sheet(''.join(lst))
                    if verbose == 1:
                        print "Created a new sheet element with id: " + str(line)
                elif count == 1:
                    # This is a unique question id (with respect to the sheet id)
                    del lst[0]
                    previousQuestion = Question(''.join(lst))
                    previousSheet.addQuestion(previousQuestion, verbose)
                    if verbose == 1:
                        print "Created a new question with id: " + ''.join(lst)
                elif count == 2:
                    # This is either a question type or question answer. Answers will have a '[' in front of them.
                    if lst[2] == '[':
                        del lst[0:3] # Remove the leading spaces and '['
                        previousQuestion.setAnswer(''.join(lst))
                        if verbose == 1:
                            print "Added answer " + ''.join(lst)
                    else:
                        del lst[0:2] # Remove the leading spaces
                        previousQuestion.setType(''.join(lst))
                        if verbose == 1:
                            print "Added type " + ''.join(lst)
                    previousSheet.setQuestion(previousQuestion.getID,previousQuestion) # Update the question with the new datasets
                    if verbose == 1:
                        print "Updated question"
            if verbose == 1:
                print ""

    def getSheets(self):
        return self.sheets

    def getSheetByID(self, id):
        for sheet in self.sheets:
            if int(sheet.getSheetID()) == int(id):
                return sheet
        print "No sheet with id " + str(id) + " found! Issues will likely arise!"

# The main test area
file = open("test_data.dat")
loader = Loader(file)
loader.parse(VERBOSE_OFF)
loader.getSheetByID("00000001").getQuestions(VERBOSE_OFF)
for question in loader.getSheetByID("00000001").getQuestions(VERBOSE_OFF):
    if int(question.getID()) == 003:
        print question.getAnswer()
