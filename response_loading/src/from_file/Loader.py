# Find example dataset in root directory named dataset_1.example
from Sheet import Sheet
from Question import Question

class Loader():

    def __init__(self, srcFile):
        self.srcFile = srcFile
        self.sheets = [ ]

    def parse(self):
        # load = self.srcFile.readline()
        previousSheet = Sheet("00000000") # Create some temp variables until proper checking can be put into place
        previousQuestion = Question("000")
        for line in self.srcFile: # Loop through all the lines in the file
            lst = list(line)
            if lst[0] == '#':
                print "Comment found" # Check if the line is a comment
            else: # If not, continue working on it
                count = 0 # Create a variable to store the indent level
                for c in lst:
                    if c == ' ':
                        count += 1 # Add to the indent level
                    else:
                        break
                print "Found " + str(count) + " spaces"
                if count == 0:
                    # This is a sheet id number (universally)
                    print "Entering Bermuda triangle"
                    if len(previousSheet.getQuestions()) != 0:
                        self.sheets.append(previousSheet)
                        print "YESSSSSSSSSSS" + str(len(previousSheet.getQuestions()))
                    else:
                        print "NOOOOOOOOOOOO" + str(len(previousSheet.getQuestions()))
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
                        del lst[0:3] # Remove the leading spaces and '['
                        previousQuestion.setAnswer(''.join(lst))
                        print "Added answer " + ''.join(lst)
                    else:
                        del lst[0:2] # Remove the leading spaces
                        previousQuestion.setType(''.join(lst))
                        print "Added type " + ''.join(lst)
                    previousSheet.setQuestion(previousQuestion.getID,previousQuestion) # Update the question with the new datasets
                    print "Updated question"
            print ""

    def getSheets(self):
        return self.sheets

    def getSheetByID(self, id):
        for sheet in self.sheets:
            if int(sheet.getSheetID()) == int(id):
                print "Found match between " + str(id) + " and " + sheet.getSheetID()
                return sheet
            else:
                print "Test" + id
                print "Test" + sheet.getSheetID();
                print "Did NOT find match between " + str(id) + " and " + sheet.getSheetID()
        print "Looking of id " + str(id)

# The main test area
file = open("test_data.dat")
loader = Loader(file)
loader.parse()
loader.getSheetByID("00000001").getQuestions()
for question in loader.getSheetByID("00000001").getQuestions():
    if int(question.getType()) == 00:
        print question.getAnswer()
