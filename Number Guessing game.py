"""
Alexander Lumala
10/19/23
Number Guessing Game
"""

import random
import statistics
from statistics import mode
def end():
    print("GAME OVER")
'This Function is called anytime the game needs to end'

def search_guess_list():
    search_number = int(input("What number would you like to find: "))
    if search_number in guess_list:
        position = guess_list.index(search_number) + 1
        print("The number",(search_number)," is in the list and you guessed it on try number", (position))
    else:
        print("This number is not in your guess list")
    print("The full guess list:", (guess_list))
"This function is called to search the guess list for specific numbers"


def most_common():
    return(mode(feedback_list))
"This fucntion says what the most common feedback was"

"This loop will only break if you tell the game to end, it basically is the entire game"
loop = True
while loop is True:

    guess_list = []
    feedback_list = []
    one = 20
    two = 10
    number = random.randrange(0,50)
    print("Welcome to the Number Guessing Game! Note, the answer is always positive and if you pick a number not in the range provided, this game will end.")
    guess = int(input("Pick a number between 0 and 50: "))
    "Now we start a loop that can only be broken by getting the correct guess"
    while number != guess:
        hint = (
            random.randint(int(number-one), int(number-two)), random.randint(int(number+two), int(number+one))
            )
        hint2 = 0
        if number < guess:
            hint2 = "Too High"
        if number > guess:
            hint2 = "Too Low" 
        if not 0 <= guess < 50:
            print("Thats not a number in the range")  
            break
        feedback_list.append(hint2)
        guess_list.append(guess)  
        "This adds your guess to the guess list"
        print("That was not the correct number, so here's a new range for you: ", hint)
        print("Here's a hint, your previous number was ", hint2)
        guess = int(input("Pick a number in the new range: "))
        if not hint[0] <= guess <= hint[1]:
            print("Thats not a number in the range, retry")  
            break
        one /= 2
        two /= 2
        "These two variables will make your range smaller and smaller every time"
    if number == guess:
        guess_list.append(guess)
        print("That was the correct Number")
        print("Congrats! It took you", len(guess_list), "guesses.")
        print("Your most common problem was: ", most_common())
        answer = input("Would you like to find a specific number in your guess list? Input either 'Yes' or 'No': ")
        if answer.lower() == 'yes':
            search_guess_list()
    
    real = input("Would you like to go again? Say either 'Yes' or 'No': ")
    if real.lower() == 'yes':
        loop = True
    else:
        end()
        loop = False
    "This section will make it so the code will repeat if you say yes or just stop if you say no"
