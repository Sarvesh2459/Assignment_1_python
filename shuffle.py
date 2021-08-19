import random
def distribute(deck_list , name):
    return {" Bot1" : deck_list[0:13] , " Bot2" : deck_list[13:26] , " Bot3" : deck_list[26:39] , name : deck_list[39:52]}
deck = open('deck.txt' , 'r')
deck_list = deck.readline().split()
random.shuffle(deck_list)
seat = deck.readline().split()
random.shuffle(seat)
print(seat)