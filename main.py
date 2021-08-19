import random
order = ['A' , 'K' , 'Q' , 'J' , 10 , 9 , 8 , 7 , 6 , 5 ,4 ,3, 2]
def startmatch(start , turn , cards , seat):
    print("Start " , start)
    print("Turn " , turn )
    cnt = 0
    seat = seat + seat
    while cnt<4:
        ind = seat.index(start)
        for card in cards[seat[ind]]:
            for i in order:
                if card[1] == i:
                    

