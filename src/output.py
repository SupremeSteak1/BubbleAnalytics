from __future__ import print_function
from resp_file_Loader import Loader as FileLoader
from resp_img_Loader import Loader as ImgLoader

class Output:

    def __init__(self):
        self.strLimit = 35
        print("Output instance initialized")
        for i in range(30):
            print()
        self.file = open("test_data.dat")
        self.loader = FileLoader(self.file)
        self.loader.parse(0)
        x = 0
        big_arr = []
        for s in self.loader.getSheets():
            x = x + 1
            y = 0
            tmp_arr  = [s.getSheetID().rstrip()]
            for question in s.getQuestions(0):
                y = y + 1
                tmp_arr.append(question.getAnswer().rstrip())
            big_arr.append(tmp_arr)
        self.displayGridOutput(big_arr)
        print()
        print()


    def getLongestLength(self,arr):
        longestValue = 0
        for inst in arr:
            if len(inst) > longestValue:
                longestValue = len(inst)
        if(longestValue>self.strLimit):
            longestValue = self.strLimit
        return longestValue

    def displayGridOutput(self,output):
        colWidths = []
        for inst in output:
            colWidths.append(self.getLongestLength(inst))
        self.printBarrier(colWidths)
        for y in range(self.getLongestLength(output)):
            for x in range(len(output)):
                print("|",end="")
                try:
                    if len(output[x][y]) > self.strLimit:
                        print(output[x][y][:self.strLimit-3]+"...",end="")
                    else:
                        print(output[x][y],end="")
                except:
                    print("",end="")
                try:
                    for i in range(colWidths[x]-len(output[x][y])):
                        print(" ",end="")
                except:
                    for i in range(colWidths[x]):
                        print(" ",end="")
            print("|")
            self.printBarrier(colWidths)


    def printBarrier(self, colWidths):
        for col in colWidths:
            print("+",end="")
            for i in range(col):
                print("-",end="")
        print("+")
Output()
