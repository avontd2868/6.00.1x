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

if 'h':
	low = guess
elif 'l':
	high = guess
elif 'c':
	game over, print guess