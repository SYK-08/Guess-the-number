import random

random_no = random.randint(1,10)
tries = 0

Name = input('Welcome, please enter your name:')
welcome = input('Hey '+ Name + ' will you play a small game with me?(y/n)')

if welcome=='n':
    print('Oh okay, bye.')
elif welcome=='y':
    guess = int(input('Great! I am thinking of a number between 0-11 try to guess it:\n'))
    if guess>random_no:
        print('Try a smaller number.')
    elif guess<random_no:
        print('Try a larger number.')
    elif guess==random_no:
        print('-------------------------------------------')
        print('Hurray!')
        print('The number was ' + str(random_no)+ ' and you did it in '+ str(tries)+' tries')
        print('-------------------------------------------')

while guess!=random_no:
    tries+=1
    guess = int(input('Try again:'))
    if guess>random_no:
        print('Try a smaller number.')
    elif guess<random_no:
        print('Try a larger number.')
    elif guess==random_no:
        print('-------------------------------------------')
        print('Hurray!')
        print('The number was ' + str(random_no)+ ' and you did it in '+ str(tries)+' tries')
        print('-------------------------------------------')
