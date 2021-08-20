import random

def startmatch(start , cards):
    order = ['A' , 'K' , 'Q' , 'J' , 10 , 9 , 8 , 7 , 6 , 5 ,4 ,3, 2]
    cnt = 0
    if start != "Player":
        for i in order:
            for j in cards[start]:
                if j[1] == i:
                    return j
    else:
        return input()

