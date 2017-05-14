# *************************************
# Shih-Chun Huang
# date 10/10/2015
# file: game.py
#
# This program is part of my second homework for Python
# This file includes functions that help run 
#   a number guessing game called "bulls and cows"
#   main(), play_game() and check_4digit()
#
#***************************************

import bulls_and_cows as bc

def main():
# Do not change this function!
    print('Welcome to Bulls and Cows death match!')
    again='y'
    while (again=='y'):
          play_game()
          again=input('would you like to play again? (y/n)')
    print('So long sucker!')


def play_game():
# plays one interactive game of bulls and cows on the console  
    answer = bc.generate_secret()
    # secret number created by Computer
    guess = check_4digit(input('Guess a 4-digit secert number:'))
    # ask players to input number and check if the input is correct 
    #   by using check_4digit funciton
    
    found = False # secret number is not yet found
    sucker = False # player is still playing (when ask if they want to continue with y/n)
    times = 0 # to record how many times has a player guessed
    
    while not found and not sucker:
        print(bc.how_many_bulls(answer,guess), 'bull(s)')
        # check how many bulls
        print(bc.how_many_cows(answer,guess), 'cow(s)')
        # check how many cows
        times = times + 1
        # increment number of guessess
        if answer == guess: 
            found = True
            print ('Congrats! You got it! (After ' + str(times) + ' guess(es).)')
        else:
            guess_again=input('Too bad, '+ str(times) +' guess(es) so far!'\
            'Would you like to guess again? (y/n)')
            
            while True:# check if the input is y/n
                if guess_again == 'y':
                    guess = check_4digit(input(str('Try a different 4-digit'\
                    'number:')))
                    # ask players to input number and check if the input is correct 
                    #   by using check_4digit funciton
                    break
                elif guess_again == 'n':
                    sucker = True
                    break
                else:
                    guess_again = input('I don\'t understand you.'\
                    'Would you like to guess again? y/n?')
                    next
        next

def check_4digit(guess):
# this function is created for checking if players input correctly
    
    while True: # check if players input number
        try:
            int(guess)
        except ValueError:
            guess = input('Not an integer!Please enter again:')
            continue
        else:
            break
        
    while len(guess) != 4: # check if players input 4 digit number
        guess = input(str('This is not a 4-digit number.'\
        'Please enter again a 4-digit number:'))
        
    return guess
    
    
# call the main function to run the game
main()
