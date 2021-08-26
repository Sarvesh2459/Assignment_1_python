import random, main
def lowest(curr , cards ,  series = ''):
    order = ['2' , '3', '4' , '5' , '6' , '7' , '8', '9' ,'10' , 'J' , 'Q' , 'K' ,'A']
    if (not(series)):
        if curr != "Player":
            for i in order:
                for j in cards[curr]:
                    if j[1:] == i :
                        return  j
        else:
            move = input()
            return  move
    else:
        if curr != "Player":
            for i in order:
                for j in cards[curr]:
                    if j[1:] == i and j[0] == series:
                        return  j
        else:
            move = input()
            return move
    for i in order:
        for j in cards[curr]:
            if j[1:] == i :
                return  j
def currmatch(curr , cards , series = '' ):
    order = ['A' , 'K' , 'Q' , 'J' , '10' , '9' , '8' , '7' , '6' , '5' ,'4' ,'3', '2']
    orderrev = ['2' , '3', '4' , '5' , '6' , '7' , '8', '9' ,'10' , 'J' , 'Q' , 'K' ,'A']
    if (not(series)):
        if curr != "Player":
            for i in order:
                for j in cards[curr]:
                    if j[1:] == i :
                        return j
        else:
            move = input()
            return move
    else:
        if curr != "Player":
            for i in order:
                for j in cards[curr]:
                    if j[1:] == i and j[0] == series:
                        return j
        else:
            move = input()
            return move
    for i in orderrev:
        for j in cards[curr]:
            if j[1:] == i :
                return  j

def checkcard(player , cards ,card1 ,card2):
    order = ['2' , '3', '4' , '5' , '6' , '7' , '8', '9' ,'10' , 'J' , 'Q' , 'K' ,'A']
    if player!= "Player" :
        if order.index(card2[1:]) > order.index(card1[1:]):
            return card2
        else:
            return main.lowest(player, cards , card2[0] )
    else :
        return card2

def winner(moves):
    list1=['A','K','Q','J','10','9','8','7','6','5','4','3','2']
    for j in list1:
        for i in moves:
            if moves[i][1:]==j:
                return i