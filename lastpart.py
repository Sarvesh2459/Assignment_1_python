
def winner(moves):
    list1=['A','K','Q','J','10','9','8','7','6','5','4','3','2']
    for j in list1:
        for i in moves:
            if moves[i][1:]==j:
                return i
