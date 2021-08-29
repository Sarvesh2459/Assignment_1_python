import random , main

def distribute():
    print('\nDo you want read from file ?')
    on = input('\nY/N : ')
    deck = open('d.txt' , 'r')
    deck_list = deck.readline().split()
    seat = deck.readline().split()
    if on!='Y' and on!='y':
        random.shuffle(deck_list)
        random.shuffle(seat)
    return {"Bot1" : deck_list[0:13] , "Bot2" : deck_list[13:26] , "Bot3" : deck_list[26:39] , "Player" : deck_list[39:52]} , seat


def starter():
    global cards
    global seat
    global winner
    global wins
    global calls
    cards , seat = distribute()
    # order = ['2' , '3', '4' , '5' , '6' , '7' , '8', '9' ,'10' , 'J' , 'Q' , 'K' ,'A']
    global calls
    # print(seat)
    seat = seat + seat
    winner = seat[0]
    wins = {'Bot1' : 0 , 'Bot2' : 0 , 'Bot3' : 0 , 'Player' : 0}
    print('\nYour Cards are = ')
    print(cards["Player"] ,"\n")
    calls = main.call_players(cards)
    print('Call of Players = ' , end=' ')
    for i in calls:
        print(i,":",calls[i] , end= ' ')
    print('\nCyclic Order')
    for i in range(4):
        print(seat[i] ,end = '->')
    print('...')
    print('\nStart from ',winner)

cont = "Y"
turn = 1
starter()
total_scores = {'Bot1' : 0 , 'Bot2' : 0 , 'Bot3' : 0 , 'Player' : 0}
while cont == "Y" or cont == "y" :
        moves = {}
        for j in cards:
            print(cards[j])
        print()
        print("\nTurn : " ,turn)
        print()
        c=1
        if(turn!=1):
            print('Your Cards are = ')
            print(cards["Player"])
        print()
        c=1
        while (c==1):
            try:
                card0 = main.currmatch(winner, cards, series = '' )
                if (winner == 'Player'):
                        pass
                else:
                    print(winner , ' : ',card0)
                cards[winner].remove(card0)
                c=0
            except ValueError:
                    print("\ncard NOt Found")
                    print('Choose another card\n')
                    c=1
        moves[winner] = card0
        cnt = seat.index(winner)
        for i in range(1,4):
            c=1
            cnt += 1
            while (c==1):
                try:
                    card = main.currmatch(seat[cnt] ,cards , card0[0])
                    winner = main.winner(moves,card0[0])
                    card = main.checkcard(seat[cnt] , cards ,moves[winner] ,card)
                    if (seat[cnt] == 'Player'):
                        pass
                    else:
                        print(seat[cnt] , ':',card)
                    cards[seat[cnt]].remove(card)
                    moves[seat[cnt]] = card
                    c=0
                except ValueError:
                        print("\nCard Not Found in Deck")
                        print('Choose another card (May be Write in Capital Letters)\n')
                        c=1
        winner = main.winner(moves,card0[0])
        print()
        print(winner , ' Wins')
        wins[winner] +=1
        if turn == 13:
            scores=main.score (calls,wins) 
            print('Scores : ')
            for i in scores:
                print(i," : " ,scores[i])
            max_score = 0
            for i in scores:
                total_scores[i] += scores[i]
                if scores[i]>max_score:
                    max_score=scores[i]
                    win = i
            print(win, ' is the winner!!!!!!!')
            cont = input("Do you want to continue? Y/N : ")
            if(cont != "Y" and cont != "y"):
                continue
            turn = 1
            starter()
            continue
        turn +=1
        print()
else:
    max_score_total = 0
    for i in total_scores:
                if total_scores[i]>max_score_total:
                    max_score_total=total_scores[i]
                    win_total = i

    print('\n\n' ,win_total, ' wins the series')