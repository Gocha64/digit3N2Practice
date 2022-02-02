import random


def digit3Subtract():    
    a = b = 0
    while True:
        a = random.randrange(100,1000)
        b = random.randrange(100,a+1)

        ma = a%100
        mb = b%100

        #대부분의 경우 받아내림 존재
        if ma < mb:
            break


    return "%5d" %a,"-%4d" %b
