def board(xstate,Ostate):

    zero='X' if xstate[0] else ('O' if Ostate[0] else 0)
    one='X' if xstate[1] else ('O' if Ostate[1] else 1)
    two='X' if xstate[2] else ('O' if Ostate[2] else 2)
    three='X' if xstate[3] else ('O' if Ostate[3] else 3)
    four='X' if xstate[4] else ('O' if Ostate[4] else 4)
    five='X' if xstate[5] else ('O' if Ostate[5] else 5)
    six='X' if xstate[6] else ('O' if Ostate[6] else 6)
    seve='X' if xstate[7] else ('O' if Ostate[7] else 7)
    eight='X' if xstate[8] else ('O' if Ostate[8] else 8)

    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seve} | {eight} ")
    
    
def win(xstate,Ostate):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in wins:
        if ((xstate[i[0]]+xstate[i[1]]+xstate[i[2]])==3):
            return 1
        if ((Ostate[i[0]]+Ostate[i[1]]+Ostate[i[2]])==3):
            return 0
    return -1   
def game():
    xstate=[0,0,0,0,0,0,0,0,0]
    Ostate=[0,0,0,0,0,0,0,0,0]
    ch=0
    turn=1

    while True:
        if turn ==1:

            board(xstate,Ostate)
            print("X turn:")
            xpos=int(input("enter the position of x"))
            xstate[xpos]=1
            ch+=1
            #print(ch)
        
        else:
            board(xstate,Ostate)
            print("O turn:")
            opos=int(input("enter the position of o"))
            Ostate[opos]=1
            ch+=1
            print(ch)
        c =win(xstate,Ostate)
        if c!=-1:
            if turn==1:
                print("match over,X won")
            elif turn==0:
                print("match over,O won")

            break
        if ch==9:
            print("tie")
            break
            

        
        turn=1-turn

game()