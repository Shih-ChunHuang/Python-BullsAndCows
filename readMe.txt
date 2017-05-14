Creator: Shih-Chun Huang
The last update:10/11/2015 

TWO PYTHON FILES
————————————————————————————————
There are two python files in this folder. One is called “bulls_and_cows”, and the other is called “game”. 

HOW DO YOU PLAY BULLS AND COWS
————————————————————————————————
Game python file is which you run if you want to play “Bulls and Cows”. Open game python file for playing the game and also keep game python file in a folder where bulls_and_cows python file is. 

The game works as follows: The computer generate a “unique” 4-digit number in secret.  The player then guesses the number and the computer provides the number of matching digits. If the matching digit is in the right position it is a "bull", if it is on a different position it is a "cow".

DESIGN DECISION 
———————————————————————————————-
About bulls_and_cows python file, it was created in order for game python file to run successfully. There are three functions in the file, which play the role of the computer. The first function is generate_secret, which the computer generates a secret number and the 4-digit number has to be unique. The second function is how_many_bulls, which the computer tells you how many bulls you get from your guess. The third function is how_many_cows, which the computer tells you how many cows you get from your guess. If a digit gets a bull, then it is not a cow because bulls trump cows. For example, if the input is 2211 and the secret number 2643, the computer gives only 1 bull instead of 1 bull 1 cow. 

About game python file, it also has three functions. One is main, which provides introduction for the game. Another is play_game, which is the game itself, including the use of functions that are in bulls_and_cows python file. Specifically, play_game function takes in the output of secret number, and the guess of input that players enter. And, play_game continually compares the secret number and the guess. Players will know how many times they have guessed while guessing. The players have chance to exit the game after each time they guess, so they don’t have to finish the game until they get the correct number. 

CONCLUSIONS FROM EXPERIMENTS 
—————————————————————————————————
In bulls_and_cows python file, the author imported two modules, one is random and the other is numpy. Module random is for the purpose of having the computer generate a 4 digit number in secret for plays to guess. And, for module numpy, it is imported for a numpy.unique function that the author can use it to make a 4 digit number unique if players intent to enter double, triple or four times of a digit. For example, if players enter 2211 and the secret number is 2105, the computer will tell the players that they get 1 bull and 1 cow instead of 1 bull and 3 cows. 

In game python file, the author imported module bulls_and_cows in order to take in the functions that are in bulls_and_cows python file. In game_play function, generate_secret function is used for the input of the secret number makes by the computer and how_many_bulls and how_many_cows are used for comparing and checking between the secret number and the guess. In order to let players know how many times have they guessed already, so there is a variable called times, which increment whenever players decide to guess again the same secret number. As to variable 

Finally, in game python file, there is a check_4digits function, which is used for checking if players enter what the computer wants them to enter. Because of this function, the game won’t stop only due to situations like players entering digits while asked to enter y/n. Specifically, not only the data type is checked and the length is checked as well. 





