# http://www.codeskulptor.org/#user38_YOYELUoekhwpYas_0.py

###some falses down there.
#Import the modules that we need.
import math
import simplegui
import random

#Setting up the global variables in our game,
# all of them have a default value 0.
# n means numbers of the remaining guesses. 

secret_number = 0
n = 0
high = 0
low = 0

####new_game() is not completed yet.
####background is not in color black.

def new_game():
    global high
    if high == 1000:
        return range1000()
    else:
        return range100()

def range100(): 
    print ""
    global secret_number, n, high, low
    high = 100
    low = 0
    n = math.log(high - low + 1) / math.log(2)
    n = int(math.ceil(n))
    secret_number = random.randrange(low, high)
    print "New game. Range is from 0 to 100"
    print "Number of remaining guesses is ", n

def range1000():
    print ""
    global secret_number, n, high, low
    high = 1000
    low = 0
    n = math.log(high - low + 1) / math.log(2)
    n = int(math.ceil(n))
    secret_number = random.randrange(low, high)
    print "New game. Range is from 0 to 1000"
    print "Number of remaining guesses is", n
    
def decrement():
    global n
    n = n - 1
    return n

def input_guess(guess):
    print ""
    print "Guess was ", guess
    remaining_guesses = decrement()
    guess = int(guess)
    if remaining_guesses >= 0:
        if guess > secret_number:
            print "Number of remaining guesses is", remaining_guesses
            print "Lower!"
        elif guess < secret_number:
            print "Number of remaining guesses is", remaining_guesses
            print "Higher!"
        else:
            print "Number of remaining guesses is", remaining_guesses
            print "Correct!"
    else:
        print "You ran out of guesses. The number was ", secret_number
        return new_game()
    
           


frame = simplegui.create_frame('Guess the number', 200, 200)
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)
frame.start()
new_game()
