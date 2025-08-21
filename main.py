import random
def guess_the_number():
    secret_number= random.randint(1,10)
    attempts=0
    print("Welcome to the Number Guessing game.")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while True:
        try:
            #Get the input from the player
            guess=int(input("Enter the guess:"))
            attempts+=1
            #check if the guess is correct, too high or too low
            if guess<secret_number:
                print("Too Low! Try Again.")
            elif guess>secret_number:
                print("Too High! Try Again.")
            else:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")
guess_the_number()