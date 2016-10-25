# This class represents one sheet, which is loaded from either a file or an image

class Sheet():

    def __init__(self, sheetID):
        self.questions = [ ]
        self.sheetID = sheetID

    def getSheetID(self):
        return self.sheetID

    def addQuestion(self, question, verbose):
        self.questions.append(question)
        if verbose == 1:
            print "Added a question to sheet " + self.getSheetID()

    def setQuestion(self, questionID, question):
        for i in range(0,len(self.questions)):
            if self.questions[i].getID() == questionID:
                questions[i] = question
                return

    def getQuestions(self, verbose):
        if verbose == 1:
            print "Has " + str(len(self.questions)) + " questions in the questions array of sheet " + self.getSheetID()
        return self.questions
