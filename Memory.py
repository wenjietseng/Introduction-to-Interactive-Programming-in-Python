#http://www.codeskulptor.org/#user38_d8M8BjOqrv_3.py
#above is the correct one, the link below contains failures
#http://www.codeskulptor.org/#user38_kVuxSinMgQrde50.py

import simplegui
import random

number = range(8) + range(8)
random.shuffle(number)
exposed = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
state = 0
first_card = 0
second_card = 0
turns = 0
# helper function to initialize globals
def new_game():
    global number, exposed, state, turns
    random.shuffle(number)
    state = 0
    turns = 0
    label.set_text("Turns = " + str(turns))
    exposed = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

def increment():
    global turns
    turns += 1

# define event handlers
def mouseclick(pos):
    global state, first_card, second_card, exposed, turns, i, j
    if state == 0:
        i = pos[0] // 50
        first_card = number[i]
        exposed[i] = True
        state = 1
    elif state == 1:
        j = pos[0] // 50
        if exposed[j] == False:
            increment()
            label.set_text("Turns = " + str(turns))
            exposed[j] = True
            second_card = number[j]
            state = 2
        else:
            state = 1
    else:
        if first_card != second_card:
            exposed[i] = False
            exposed[j] = False
            i = pos[0] // 50
            if exposed[i] == False:
                exposed[i] = True
                first_card = number[i]
                state = 1
            else:
                state = 2
        else:
            i = pos[0] // 50
            if exposed[i] == False:
                exposed[i] = True
                first_card = number[i]
                state = 1
            else:
                state = 2
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for num in range(len(number)):
        canvas.draw_text(str(number[num]), [15 + 50 * num, 60], 40, "White")
        if exposed[num] == False:
            canvas.draw_polygon(([0 + 50*num, 0], [0 + 50*num, 100], [50 + 50*num, 100], [50 + 50*num, 0]), 1, "Green", "Green")
    for num in range(len(number)-1):
        canvas.draw_line([50 + 50*num, 0],[50 + 50*num, 100], 2, "Black")    
   
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
