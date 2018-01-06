from random import randint as rd

miniNum = 1
maxNum = 6
pl_score=-1
pl_score2=-1
com_score=-1
wins = 0
lost = 0

'''def winned():
    wins+=1
    return wins
'''
def rolling() :
    dice_Num = rd(miniNum,maxNum)
    return dice_Num                                                                                                                                                                                 

def pl_roll(numb):
    num = rolling()
    print('The dice rolled',num,' this time')
    numb += num
    pl_score = numb
    return pl_score

def comp_roll(numb1):
    num1=rolling()
    print('Dice rolled ',num1, 'for computer')
    numb1 += num1
    com_score=numb1
    return com_score

def pl_roll2(numb2):
    num2=rolling()
    print('Dice rolled ',num2, 'for ',player_2)
    numb2 += num2
    pl_score2 = numb2
    return pl_score2

print('Please register by entering your name')
player_1=input(':-')
    
print("Choose the mode of play  ")
print('1. Computer ')
print('2. Multiplayer')
print('3. Exit')
mode = input(':-')

if mode == '1':
    print('Two contenders of the match are :-\n',player_1,'\nComp')
    print('hey!!...Should we start the game')

elif mode == '2':
    player_2 = input('Enter the name of the second player\n:-')
    print("The two players of the match are:- \n",player_1,"\n",player_2)
    print("\n\nHey",player_1,"and ",player_2)
    print("Let's begin the war")
    
else :
    exit()

space = input("Press 'r' to know the rules\n:-")
if space == 'r' :
    print('Initially your score is 0\nand you have to score  30 points by rolling the dice\nbefore your oponent does')
    print('All the best')
else:
    pass

if mode == '1':
    while pl_score<=30 and com_score<=30 :
        print("\n\nHey",player_1,"\nTap '1' to roll the dice else type '0' to terminate")
        turn = input(':-')
        if turn =='1':
            pl_score = pl_roll(pl_score)
            print('Your  score is ',pl_score)
        
        elif turn =='0':
            exit()
        else:
            print("Alright get out from here..\n cause you are a bit annoying ")

        print('\nThe comp needs your permission to roll the dice')
        roll = input("Type ' ' to grant access\n:-")
        if roll == ' ':
            com_score = comp_roll(com_score)          
            print('The computer score is ',com_score)
        else :
            break
            print('You cannot play the game this way')

    if pl_score>com_score:
        print('\nCongratulations\nYou have beaten the computer by',pl_score - com_score,'points')
        wins+=1
    else:
        print('\nComputer knows better how to roll the dice\nCome back to win next time') 
        lost+=1

elif mode == '2':
    while  pl_score<30 and pl_score2<30 :
        print('\n',player_1,"will roll the dice by pressing no. 1")
        turn = input(':-')
        if turn =='1':
            pl_score = pl_roll(pl_score)
            print('Your  score is ',pl_score)
        else :
           print('Now u have started the game...\n must afraid to finish it ')
           exit()

        print('\nNow',player_2,"will roll the dice by entering '2' ")
        turn1 = input(':-')
        if turn1 == '2':
             pl_score2 = pl_roll2(pl_score2)     
             print(player_2,' score is ',pl_score2)
        else :
            break

    if pl_score > pl_score2 :
        print("well done",player_1,'\nYou have beaten ',player_2,'by',pl_score-pl_score2,'points')
        wins+=1
    elif pl_score==pl_score2 :
        print('That was a tight match\nPlay again to decide a winner')
    else :
        print(player_2 ,'have beaten ',player_1,'by',pl_score2-pl_score,'points\nWell played')
        lost+=1
else:
    print('Go home and prepare for this game')


win=input('Do u want to know the results\n:-')
if win == 'yes' or win =='y' :
    print('The number of matches u have won are',wins)
else :
    print('Alright...we know its a hard time for you')


        
'''    

'f user==1 :                                                                              #check the conditon
    print('Rolling the dice')
  
    while roll == 'yes' or roll == 'y' :
  
        

        if dice_Num >3:                                                              #cases starts with if
            print('These are pretty good numbers...!!')

        elif dice_Num ==  2 or dice_Num ==3 :
            print('You need to improve these numbers     Better luck next time')

        else :
            print('Getting 1','Not many people can roll it')
        
        roll = input('Do u wanna roll it again ?')                        #this checks the while condition
else:
    print('come back to play next time')
'''
