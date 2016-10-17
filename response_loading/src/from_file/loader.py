# Find example dataset in root directory named dataset_1.example

class Loader():

    def __init__(self, srcFile):
        self.srcFile = srcFile

    def parse(self):
        self.srcFile.read()
