import random
print("Welcome to the Number Guessing game.")
def main():
    run_game()
    play_again()

def run_game():
    counter = 1
    random_no = random.randint(1,10)
    while counter > 0 and counter <=5:
        guess = int(input("Try to guess the number:\n"))
        if guess != random_no and guess > random_no:
            print("Wrong number.Try a lower value.")
            counter += 1
        elif guess != random_no and guess < random_no:
            print("Wrong number.Try a higher value.")
            counter += 1
        else:
            print("Well done! The number was ", str(random_no), " and you did it in " ,str(counter), " attempts.")
            
            play_again()
        
        if counter == 2:
            print("4 attempts left before the program ends.")
        if counter == 3:
            print("3 attempts left before the program ends.")
        if counter == 4:
            print("2 attempts left before the program ends.")
        if counter == 5:
            print("1 attempt left before the program ends.") 

def play_again():
    while True:
        Q = input('Would you like to play again?(y/n):')
        if Q == 'y':
            main()
        if Q == 'n':
            exit()       
        else:
            print("Invalid input")
main()
