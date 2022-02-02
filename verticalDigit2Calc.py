import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from verticalDigit3Calc import verticalDigit3Calc
from digit2Subtract import digit2Subtract
from digit2Add import digit2Add
import docx
import random
import verticalAnswerForDigit3N2Calc

class verticalDigit2Calc(verticalDigit3Calc):
    fileName = "digit2Calc"

    def __init__(self, baseForPracticeDocxName, baseForAnswerDocxName):
        verticalDigit3Calc.__init__(self, baseForPracticeDocxName, baseForAnswerDocxName)
        
    def getProblem(self):
        flag = random.randrange(0,2) #0 -> +, 1 -> -
        if flag == 0:
            c = digit2Add()

        else:
            c = digit2Subtract()

        return c


if __name__ == '__main__':
    asdf = verticalDigit2Calc('baseForAddNSubtract.docx', 'baseForVerticalAnswer.docx')
    print(asdf.fileName + " generator")
    i = int(input('생성 할 문제 수(1page = 30문제): '))
    asdf.digitNCalc(i)
