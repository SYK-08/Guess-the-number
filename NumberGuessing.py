import random

random_number = random.randint(1,10)
tries = 0

username = input('Please enter your username:')

print('Hello '+ username +' !')

question = input('Would you like to play a small game?(y/n):')

if question=='n':
    print('Okay, no problem.')

elif question=='y':
    print('Hurray! Lets go then.')
    print('I am guessing a number between 1-11.')
    guess = int(input('Have a guess:'))
    if guess>random_number:
        print('Try a smaller number.')
    elif guess<random_number:
        print('Try a larger number.')
    elif guess==random_number:
        print('Awesome! you got it. The number was ',random_number,'and ', 'you did it in ', tries,'tries.')

while guess!= random_number:
    tries += 1
    guess = int(input('Try again:'))
    if guess>random_number:
        print('Try a smaller number.')
    elif guess<random_number:
        print('Try a larger number.')
    elif guess==random_number:
        print('Awesome! you got it. The number was ',random_number,'and ', 'you did it in ', tries,'tries.')
