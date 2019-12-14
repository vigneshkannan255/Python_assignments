p1=input('Enter player 1:')
p2=input('Enter player 2:')
total=0
while(1):
    pi1=int(input('Player 1 Enter value: '))
    if(pi1 <= 10):
        total+=pi1
        print(total)
        if(total == 100):
            print(p1+':wins')
            break
        else:
            pi2=int(input('player 2 Enter value:'))
            if(pi2 <= 10):
                total+=pi2
                print(total)
                if(total == 100):
                    print(p2+':wins')
                    break 
