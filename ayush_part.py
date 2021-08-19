cards={"bot1":["HA","HJ","D10","D9","S8","DK","S5","SK","DA","CJ","C5"],"player":["HA","HJ","D10","D9","S8","DK","S5","SK","DA","CJ","C5"]}
def call_players(cards):
    dict2=dict()
    call=0
    for j in cards:
        if(j=="player"):
            call=input("enter your call")
        else:
            for i in cards[j]:
                if(i=="HA" or i=="HK" or i=="HQ" or i=="HJ" or i=="DA" or i=="DK" or i=="DQ" or i=="DJ" or i=="SA" or i=="SK" or i=="SQ" or i=="SJ" or i=="CA" or i=="CK" or i=="CQ" or i=="CJ"):
                    call+=1
        dict2[j]=call
    return dict2

print(call_players(cards))

              

        

