# This class represents one sheet, which is loaded from either a file or an image

class Sheet():

    def __init__(self):
        self.questions = [ ]

    def addQuestion(self, question):
        self.questions.append(question)
