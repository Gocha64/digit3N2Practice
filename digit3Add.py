import random


def digit3Add():
    a = b = 0
    while True:
        a = random.randrange(100,1000)
        b = random.randrange(100,1000)

        ma = a%10
        mb = b%10

        #1개 이상의 받아올림 존재
        if ma + mb > 10:
            break

            
    return "%5d" %a,"+%4d" %b
