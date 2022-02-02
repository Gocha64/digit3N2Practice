# 1문제 -> 3줄
# line 1 -> 피연산자
# line 2 -> 연산자, 피연산자
# line 3 -> 공백
# 1페이지 -> 30문제
import docx

def opcheck(line):
    o = line[0]
    b = int(line[1:])
    
    return o, b


def answering(fName):
    f1 = open(fName + '.txt', 'r')
    f2 = open(fName + "Answer.txt",'w') #txt2Docx에서 입력값으로 사용함
    line = ''
    p = 1
    f1.readline()
    
    while True:
        f2.write("page. %d\n" %p)
        p += 1
        for i in range(30):
            a = 0
            b = 0
            o = ''
            data = ''
            for j in range(3):
                line = f1.readline()
                #print(j,line)
                if not line:
                    if o == '+':
                        data = "%d+%d=%d\n" %(a,b,(a+b))
                    elif o == '-':
                        data = "%d-%d=%d\n" %(a,b,(a-b))
                    f2.write(data)
                    print(f2.name + ' generated')
                    f1.close()
                    f2.close()
                    return 0
                if j == 0:
                    a = int(line)
                elif j == 1:
                    o, b = opcheck(line)
            
            if o == '+':
                data = "%d+%d=%d\n" %(a,b,(a+b))
            elif o == '-':
                data = "%d-%d=%d\n" %(a,b,(a-b))
            
            f2.write(data)

def answerText2Docx(fName, baseDocx):
    document = docx.Document(baseDocx)
    file = open(fName + 'Answer.txt', 'r')
    document._body.clear_content()
    for line in file:
        #print('1.'+line)
        document.add_paragraph(line[:-1])
    document.save(fName + 'Answer.docx')
    print(fName + 'Answer.docx generated')
    
if __name__ == '__main__':
    #answering('세자리 + 세자리 산수.txt')
    answerText2Docx('answer.txt', 'baseForVerticalAnswer.docx')
