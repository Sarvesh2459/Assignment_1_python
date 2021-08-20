import random
def lowest(curr , cards ,  series = ''):
    order = [2 , 3, 4 , 5 , 6 , 7 , 8, 9 ,10 , "J" , 'Q' , "K" ,"A"]
    cnt = 0
    if curr != "Player":
        for i in order:
            for j in cards[curr]:
                if j[1] == i :
                    return j[0] , j
    else:
        move = input()
        return move[0] , move
def currmatch(curr , cards ,  series = ''):
    order = ['A' , 'K' , 'Q' , 'J' , 10 , 9 , 8 , 7 , 6 , 5 ,4 ,3, 2]
    cnt = 0
    if curr != "Player":
        for i in order:
            for j in cards[curr]:
                if j[1] == i :
                    return j[0] , j
    else:
        move = input()
        return move[0] , move

