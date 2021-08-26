'''c1=int(input("enter the call of player1 : "))
c2=int(input("enter the call of player2 : "))
c3=int(input("enter the call of player3 : "))
c4=int(input("enter the call of player4 : "))
dict1={"player1" : c1 , "player2" : c2 , "player3" : c3 , "player4" : c4}
w1=int(input("enter the value actual win of player1 : "))
w1=int(input("enter the value actual win of player1 : "))
w1=int(input("enter the value actual win of player1 : "))
w1=int(input("enter the value actual win of player1 : "))
dict2 = {}
'''
def score (dict1,dict2):
    dict3={}

    for i in dict1  :
        if dict1[i] > dict2[i] :
            point = -(10)*(dict1)
        else :
            point = 10(dict1[i]) + (dict2[i]-dict1[i])
        dict3[i]=point
    
    return dict3