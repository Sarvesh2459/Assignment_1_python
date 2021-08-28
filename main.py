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

def winner(moves,series):

    list1=['A','K','Q','J','10','9','8','7','6','5','4','3','2']
    for j in list1:
        for i in moves:
            if moves[i][1:]==j:
                if(series[0]==moves[i][0]):
                    return i
                
def score (dict1,dict2):
    dict3={}
    print(dict1)
    print(dict2)
    for i in dict1  :
        
        if dict1[i] > dict2[i] :
            point = -(10)*(dict1[i])
        else :
            point = 10*(dict1[i]) + (dict2[i]-dict1[i])
        dict3[i]=point
    return dict3

def call_players(cards):
    dict2=dict()
    
    for j in cards:
        if(j=="Player"):
            call=int(input("enter your call"))
        else:
            call=0
            for i in cards[j]:
                if(i=="HA" or i=="HK" or i=="HQ" or i=="HJ" or i=="DA" or i=="DK" or i=="DQ" or i=="DJ" or i=="SA" or i=="SK" or i=="SQ" or i=="SJ" or i=="CA" or i=="CK" or i=="CQ" or i=="CJ"):
                    call+=1
        dict2[j]=call
    return dict2
