import random , main
def distribute(deck_list ):
    return {"Bot1" : deck_list[0:13] , "Bot2" : deck_list[13:26] , "Bot3" : deck_list[26:39] , "Player" : deck_list[39:52]}
deck = open('deck.txt' , 'r')
deck_list = deck.readline().split()
random.shuffle(deck_list)
seat = deck.readline().split()
print(deck_list[0:13])
print(deck_list[13:26])
print(deck_list[26:39])
print(deck_list[39:52])
random.shuffle(seat)
print(seat)
cnt = 0
while cnt < 4:
    print(main.startmatch(seat[cnt], distribute(deck_list)))
    cnt += 1