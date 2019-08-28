#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!')
#this is printing the highliighted orange phrase in the terminal. 
colors = ['red','orange','yellow','green','blue','violet','purple']
#this is setting the variable, color, equal to the list following. 
play_again = ''
#this is setting the variable, play_again, equal to a space given by the quotations.
best_count = sys.maxsize      
      # this sets the variable, best_count, equal to the biggest number the program has yet seen. 
while (play_again != 'n' and play_again != 'no'):
    #this sets a condition where when play_again is not equal to 'n' and 'no', then the following lines become relevant until play_again = 'n' or 'no'
    match_color = random.choice(colors)
    #match_color returns a random item from the colors list
    count = 0
    color = ''
    while (color != match_color):
        #this sets a condition where when color does not equal a random choice from the colors list, the following lines become relevant until the input = match_color.
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        #this line indicated that the variable, color, becomes the input following the line "What is my favorite color?" in the terminal. 
        color = color.lower().strip()
        #this solves the problem presented when spaces and capitalizations are added so that many variations of the correct answer can be accepted. 
        count += 1
        #this adds 1 to the running count for every input of an answer for the variable "color"
        if (color == match_color):
            #if the variable "color" is the same as a choice in the colors list, also now equal to the variable match_color, then the program prints "correct!"
            print('Correct!')

        else:
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))
            #'''If any other answer is entered, the program will print "Sorry, try again. You have guessed", which will then use the running variable, 
            # count, in place of the word "guesses" in the code.''' 
    print('\nYou guessed it in {0} tries!'.format(count))
    #this will add a line at the end which gives the number of entries a person had made while guessing the correct color. this uses the variable count just as the line before it did.
    if (count < best_count):
        print('This was your best guess so far!') 
        best_count = count
    play_again = input("\nWould you like to play again? ").lower().strip()
    #'''this gives a variable, play_again, that will print the phrase in quotations and then allow the user to enter an answer.
    #If the answer given is anything besides "n" or "no", then the game will restart. '''
print('Thanks for playing!')
#If the answer "n" or "no" is entered, then the program will print "Thanks for playing!" and complete it's course. 