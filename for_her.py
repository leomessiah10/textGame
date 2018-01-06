from random import randint as rd

rand_num = rd(1,10)
tries = 1
condition = 1
#print(rand_num)
user_name = input("Hey !! What's your good name\n:-")
print('Hi',user_name + '.')
ques = input('Do you wish to play a game\n[Y/N]\n')

if ques == 'N' or ques == 'n' :
    print("Well..it's the best i can do\nGood Bye")
    exit

elif ques == 'Y' or ques == 'y' :
    print('Alright...its start this way ')
    print('I will guess a number between 1 to 10\n')

    while condition == 1 or tries !=6:
        guess = int(input("Make a guess of the number\n"))

        if guess > rand_num :
            print('You guessed a big number...make it small')
            tries +=1
        elif guess < rand_num :
            print('Nooooo....think of a greater number')
            tries +=1
        else :
            #printguess == rand_num :
            condition = 0
            print('Great ....You have guessed a right number')
            print('You have guessed in ',tries, 'chances')
            break
else :
    print('You are something that the world wants to get rid off')
    exit
