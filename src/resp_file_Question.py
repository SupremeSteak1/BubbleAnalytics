# This class represents question responses

class Question():

    def __init__(self, id):
        self.id = id
        self.type = "NONE"
        self.answer = "NONE"

    def getID(self):
        return self.id
    
    def hasType(self):
        return self.type != "NONE"

    def hasAnswer(self):
        return self.answer != "NONE"

    def setType(self, type):
        self.type = type

    def setAnswer(self, answer):
        self.answer = answer

    def getType(self):
        return self.type

    def getAnswer(self):
        return self.answer
