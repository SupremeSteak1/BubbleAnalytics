from resp_file_Loader import Loader as FileLoader
from resp_img_Loader import Loader as ImgLoader
import htmlPy


class BackEnd(htmlPy.Object):

    def __init__(self, app):
        self.VERBOSE_OFF = self.CHECKBOX_UNCHECKED = 0
        self.VERBOSE_ON = self.CHECKBOX_CHECKED = 1
        super(BackEnd, self).__init__()
        self.app = app

    @htmlPy.Slot()
    def say_hello_world(self):
        self.file = open("save_file.dat")
        self.loader = FileLoader(self.file)
        self.loader.parse(self.VERBOSE_OFF)
        x = 0
        for s in self.loader.getSheets():
            x = x + 1
            y = 0
            for question in s.getQuestions(self.VERBOSE_OFF):
                y = y + 1
                self.app.evaluate_javascript("setCell( \""+str(x-1)+"\" , \""+str(y-1)+"\" , \""+"Label "+str(x-1)+", "+str(y-1)+"\" );")
                print("setCell( \""+str(x)+"\" , \""+str(y)+"\" , \""+str(question.getAnswer().rstrip())+"\" );")
                self.app.evaluate_javascript("setCell( \""+str(x)+"\" , \""+str(y)+"\" , \""+str(question.getAnswer().rstrip())+"\" );")

        #self.app.html = u"Hello, world"
        """
        x = 0;
        y = 0;
        text = "Some arbitrary text";
        self.app.evaluate_javascript("setCell( \""+str(x)+"\" , \""+str(y)+"\" , \""+str(text)+"\" );")
        x = 1;
        y = 0;
        text = "Some arbitrary text to the right of the other arbitrary text";
        self.app.evaluate_javascript("setCell( \""+str(x)+"\" , \""+str(y)+"\" , \""+str(text)+"\" );")
        x = 0;
        y = 1;
        text = "Some arbitrary text below the other arbitrary text";
        self.app.evaluate_javascript("setCell( \""+str(x)+"\" , \""+str(y)+"\" , \""+str(text)+"\" );")
        print "activated"
        """
