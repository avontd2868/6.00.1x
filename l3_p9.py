# Lecture 3 Problem 9

'''

Ask user to guess a number between 0 and 100.

Guess secret_number with user hints and bisection search:

low = 0
high = 100
guess = (high + low) / 2

print guess
prompt user for hint:
    'h' - guess too high
    'l' - guess too low
    'c' - guess is correct

loop:
    if 'h':
	    guess is the new high end
    elif 'l':
	    guess is the new low end
    elif 'c':
	    game over; break and print guess

    bisect (guess = (high + low) / 2)
    print guess

'''

low = 0
high = 100
guess = (high + low) / 2

print "Please think of a number between 0 and 100!"

while True:

    print "\nIs your secret number " + str(guess) + "?"
    print "Enter 'h' to indicate the guess is too high." 
    print "Enter 'l' to indicate the guess is too low." 
    print "Enter 'c' to indicate I guessed correctly."
    hint = raw_input("\n> ")

    if hint == 'h':
    	high = guess
    elif hint == 'l':
    	low = guess
    elif hint == 'c':
    	print "Game over. Your secret number was: " + str(guess)
    	break
    else:
    	"Say what?"

    guess = (high + low) / 2




