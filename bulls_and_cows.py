
# *************************************
# Shih-Chun Huang
# date 10/10/2015
# file: bulls_and_cows.py
#
# This program is part of my second homework for Python
# This file includes functions that help run 
#   a number guessing game called "bulls and cows"
#   generate_secret(), how_many_bulls() and how_many_cows()
#
#***************************************
 
import random
import numpy # import numpy for unique function

def generate_secret():

    found = False
    while (not found):
        # generates a 4 digit number with no repaeat digits
        a = random.randint(0,9)
        b = random.randint(0,9)
        c = random.randint(0,9)
        d = random.randint(0,9)
        
        if a != b and a !=c and a !=d and b !=c and b !=d and c !=d:
        # it converts the number to a string and returns it            
            secret = str(a)+str(b)+str(c)+str(d)
            #print (secert)
            return secret



def how_many_bulls(answer,guess):
# returns the number of bulls the guess earns when the secret number is answer
    bulls = 0
    if guess[0] == answer[0]:
        # check the first digit
        bulls = bulls+1
    if guess[1] == answer[1]:
        # check the second digit
        bulls = bulls+1
    if guess[2] == answer[2]:
        # check the third digit
        bulls = bulls+1
    if guess[3] == answer[3]:
        # check the forth digit
        bulls = bulls+1
        
    return bulls



def how_many_cows(answer, guess):
# returns the number of cows the guess earns when the secret number is answer
    cows = 0
    guess_unique = numpy.unique(list(str(guess)))
    # make guess a unique 4 digit number  
    for item in guess_unique:
        for element in answer:
            # compare each digit between guess-unique and answer
            if item == element:
                cows = cows + 1
                
    cows = cows - how_many_bulls(answer, guess)
    # the comparison above also includes bulls, so need to deduct them
    return cows

