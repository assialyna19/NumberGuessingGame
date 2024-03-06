import random

def nmbr_guess_game():
    # Produce a random target number within the range of 1 to 100.
    target_number = random.randint(1, 100)
    
    print("Welcome to the Number Guessing Game!")
    print("You are given 10 chances to guess the target number within the range of 1 to 100.")
    
    attempts = 0
    while attempts < 10:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess == target_number:
                print("GG! You guessed the correct number in", attempts, "attempts!")
                return
            elif guess < target_number:
                print("The target number is greater than your guess.")
            else:
                print("The target number is less than your guess.")
        except ValueError:
            print("Input is not valid. Please provide a valid number.")
    
    print("Apologies, you have exhausted your attempts. The intended number was:", target_number)

nmbr_guess_game()
