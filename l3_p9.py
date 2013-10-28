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

    print "Is your secret number " + str(guess) + "?"
    print "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is to low. Enter 'c' to indicate I guessed correctly.",
    hint = raw_input()

    if hint == 'h':
        high = guess
    elif hint == 'l':
        low = guess
    elif hint == 'c':
        print "Game over. Your secret number was: " + str(guess)
        break
    else:
    	print "Sorry, I did not understand your input."
        continue

    guess = (high + low) / 2


