import random , main

def distribute(deck_list ):
    random.shuffle(deck_list)
    return {"Bot1" : deck_list[0:13] , "Bot2" : deck_list[13:26] , "Bot3" : deck_list[26:39] , "Player" : deck_list[39:52]}
deck = open('deck.txt' , 'r')
deck_list = deck.readline().split()
seat = deck.readline().split()
cards = distribute(deck_list)
# order = ['2' , '3', '4' , '5' , '6' , '7' , '8', '9' ,'10' , 'J' , 'Q' , 'K' ,'A']
random.shuffle(seat)
print(seat)
seat = seat + seat
cont = "Y"
turn = 12
winner = seat[0]
wins = {}
while cont == "Y" or cont == "y" :
    moves = {}
    print("Turn : " ,turn)
    print()
    for j in cards:
        print(cards[j])
    print()
    card0 = main.currmatch(winner, cards, series = '' )
    print( winner ,  card0)
    cards[winner].remove(card0)
    moves[winner] = card0
    cnt = seat.index(winner)
    print(cnt)
    for i in range(1,4):
        cnt += 1
        card = main.currmatch(seat[cnt] ,cards , card0[0])
        card = main.checkcard(seat[cnt] , cards ,card0 ,card)
        print(seat[cnt] , card)
        cards[seat[cnt]].remove(card)
        moves[seat[cnt]] = card
    winner = main.winner(moves)
    print()
    print(winner)
    if turn == 13:
        cont = input("Do you want to continue? Y/N : ")
        cards = distribute(deck_list)
        random.shuffle(seat)
    turn +=1
    print()