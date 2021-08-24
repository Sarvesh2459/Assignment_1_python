import random
def lowest(curr , cards ,  series = ''):
    order = ['2' , '3', '4' , '5' , '6' , '7' , '8', '9' ,'10' , 'J' , 'Q' , 'K' ,'A']
    if series!='':
        if curr != "Player":
            for i in order:
                for j in cards[curr]:
                    if j[1:] == i :
                        return j[0] , j
        else:
            move = input()
            return move[0] , move
    else:
        if curr != "Player":
            for i in order:
                for j in cards[curr]:
                    if j[1:] == i and j[0] == series:
                        return j[0] , j
        else:
            move = input()
            return move[0] , move
def currmatch(curr , cards , first_val , series = '' ):
    order = ['A' , 'K' , 'Q' , 'J' , '10' , '9' , '8' , '7' , '6' , '5' ,'4' ,'3', '2']
    if (not(series)):
        if curr != "Player":
            for i in order:
                for j in cards[curr]:
                    if j[1:] == i :
                        return j[0] , j
        else:
            move = input()
            return move[0] , move
    else:
        if curr != "Player":
            for i in order:
                for j in cards[curr]:
                    if j[1:] == i and j[0] == series:
                        return j[0] , j
        else:
            move = input()
            return move[0] , move

