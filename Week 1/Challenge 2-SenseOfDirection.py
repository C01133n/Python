import random

def sense_of_direction_game():
    directions = ['north', 'south', 'east', 'west']
    correct_direction = random.choice(directions)
    
    print("Welcome to the Sense of Direction Game!")
    print("I'm thinking of a direction (north, south, east, or west).")
    print("Try to guess the direction based on the clues I give you.")

    guesses = 0
    while True:
        user_guess = input("Your guess: ").lower()
        guesses += 1
        
        if user_guess == correct_direction:
            print(f"Congratulations! You guessed it right in {guesses} guesses.")
            break
        else:
            print("Oops! That's not the correct direction. Try again.")

if __name__ == "__main__":
    sense_of_direction_game()