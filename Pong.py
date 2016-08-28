# [PONG GAME]
# http://www.codeskulptor.org/#user38_9zax0HD1bSqTztV_0.py
# 1.Use "w" and "s" control the left paddle, "¡ô" and "¡õ" for the right paddle.
# 2.Set your win points, default is 5, remember to press enter for input.
# 3. Find yourself a partner and PLAY!!!!


#Original structure
#http://www.codeskulptor.org/#user38_9zax0HD1bSqTztV.py
# Implementation of classic arcade game Pong
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0.0, 0.0]
direction = "RIGHT"
ball_radius = 20
paddle1_pos = [HALF_PAD_WIDTH, HEIGHT / 2]
paddle2_pos = [WIDTH - HALF_PAD_WIDTH, HEIGHT / 2]
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == "RIGHT":
        ball_vel[0] = random.randrange(120, 240) / 60
        ball_vel[1] = -random.randrange(60, 180) / 60
    else:
        ball_vel[0] = -random.randrange(120, 240) / 60
        ball_vel[1] = -random.randrange(60, 180) / 60

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2, direction  # these are ints
    paddle1_pos = [HALF_PAD_WIDTH, HEIGHT / 2]
    paddle2_pos = [WIDTH - HALF_PAD_WIDTH, HEIGHT / 2]
    paddle1_vel = 0
    paddle2_vel = 0
    dd = random.randrange(0, 2)
    if dd == 0:
        direction = "RIGHT"
    else:
        direction = "LEFT"
    spawn_ball(direction)
    score1 = 0
    score2 = 0
        
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    global paddle1_vel, paddle2_vel, score1, score2
    upper_edge1 = paddle1_pos[1] - HALF_PAD_HEIGHT
    lower_edge1 = paddle1_pos[1] + HALF_PAD_HEIGHT
    upper_edge2 = paddle2_pos[1] - HALF_PAD_HEIGHT
    lower_edge2 = paddle2_pos[1] + HALF_PAD_HEIGHT

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[1] += paddle1_vel
    paddle2_pos[1] += paddle2_vel 
    if(paddle1_pos[1] - HALF_PAD_HEIGHT <= 0):
        paddle1_pos[1] = HALF_PAD_HEIGHT
    elif (paddle1_pos[1] + HALF_PAD_HEIGHT >= HEIGHT):
        paddle1_pos[1] = HEIGHT - HALF_PAD_HEIGHT
    if(paddle2_pos[1] - HALF_PAD_HEIGHT <= 0):
        paddle2_pos[1] = HALF_PAD_HEIGHT
    elif (paddle2_pos[1] + HALF_PAD_HEIGHT >= HEIGHT):
        paddle2_pos[1] = HEIGHT - HALF_PAD_HEIGHT    

    # update ball
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]
    if (ball_pos[1] <= ball_radius) or (ball_pos[1] >= HEIGHT - ball_radius):
        ball_vel[1] = -ball_vel[1]
    if (ball_pos[0] <= PAD_WIDTH + ball_radius):
        if (ball_pos[1] <= lower_edge1) and (ball_pos[1] >= upper_edge1):
            ball_vel[0] = -1.1 * ball_vel[0]
        else:
            score2 += 1
            spawn_ball("RIGHT")
    elif (ball_pos[0] >= WIDTH - PAD_WIDTH - ball_radius):
        if (ball_pos[1] <= lower_edge2) and (ball_pos[1] >= upper_edge2):
            ball_vel[0] = -1.1 * ball_vel[0]
        else:
            score1 += 1
            spawn_ball("LEFT")

    # draw ball
    canvas.draw_circle(ball_pos, ball_radius, 1, "White", "Orange")
    # draw paddles
    canvas.draw_polygon([(0, upper_edge1), (PAD_WIDTH, upper_edge1), (PAD_WIDTH, lower_edge1), (0, lower_edge1)], 1, 'White', 'White')
    canvas.draw_polygon([(WIDTH, upper_edge2), (WIDTH - PAD_WIDTH, upper_edge2), (WIDTH - PAD_WIDTH, lower_edge2), (WIDTH, lower_edge2)], 1, 'White', 'White')
    # draw scores
    canvas.draw_text("P1: " + str(score1), [110, 75], 30, "Red")
    canvas.draw_text("P2: " + str(score2), [410, 75], 30, "Blue")
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel -= 4.5
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel += 4.5
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel -= 4.5
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel += 4.5
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel += 4.5
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel -= 4.5
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel += 4.5
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel -= 4.5

def reset():
    new_game()
 
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset", reset, 200)
# start frame
new_game()
frame.start()
