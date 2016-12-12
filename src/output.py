from __future__ import print_function

class Output:

    def __init__(self):
        print("Output instance initialized")
        self.displayGridOutput([["test","anothertest","f",""],["testf","anotherst","fdsafds",""]])

    def getLongestLength(self,arr):
        longestValue = 0
        for inst in arr:
            if len(inst) > longestValue:
                longestValue = len(inst)
        return longestValue

    def displayGridOutput(self,output):
        colWidths = []
        for inst in output:
            colWidths.append(self.getLongestLength(inst))
        print(str(colWidths))
        for col in colWidths:
            print("+",end="")
            for i in range(col):
                print("-",end="")
        print("+")

Output()
