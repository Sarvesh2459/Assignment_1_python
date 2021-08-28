import random , main

def distribute(on):
    deck = open('deck.txt' , 'r')
    deck_list = deck.readline().split()
    seat = deck.readline().split()
    if on=='Y' or on=='y':
        random.shuffle(deck_list)
        random.shuffle(seat)
    return {"Bot1" : deck_list[0:13] , "Bot2" : deck_list[13:26] , "Bot3" : deck_list[26:39] , "Player" : deck_list[39:52]} , seat

on = input('Do you want to read cards from file? Y/N')
cards , seat = distribute(on)
# order = ['2' , '3', '4' , '5' , '6' , '7' , '8', '9' ,'10' , 'J' , 'Q' , 'K' ,'A']

print(seat)
seat = seat + seat
cont = "Y"
turn = 1
winner = seat[0]
wins = {'Bot1' : 0 , 'Bot2' : 0 , 'Bot3' : 0 , 'Player' : 0}
calls = main.call_players(cards)
print(calls)
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
    winner = main.winner(moves,card0[0])
    print()
    print(winner)
    wins[winner] +=1
    if turn == 13:
        scores=main.score (calls,wins) 
        print(scores)
        max_score = 0
        for i in scores:
            if scores[i]>max_score:
                max_score=scores[i]
                win = i
        print(i)
        cont = input("Do you want to continue? Y/N : ")
        turn = 1
        cards = distribute(on)
        random.shuffle(seat)
    turn +=1
    print()