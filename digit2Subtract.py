import random


def digit2Subtract():
    a = b = 0
    while True:
        a = random.randrange(11,100)
        b = random.randrange(10,a)
        aM = a%10 #a의 일의 자리수
        bM = b%10 #b의 일의 자리수

        if aM < bM:
            break
        else:
            d = random.randrange(0,10)
            if d > 8:
                break

        
        
    return "%4d" %a,"-%3d" %b
