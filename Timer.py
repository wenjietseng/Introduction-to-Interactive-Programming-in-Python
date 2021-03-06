# http://www.codeskulptor.org/#user38_OOUlVLf8f1_7.py

# template for "Stopwatch: The Game"
import simplegui

# define global variables
t = 0
x = 0
y = 0
original_state = False
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    if len(str(t)) == 0:
        return "0:00.0"
        
    elif len(str(t)) == 1:
        return "0:00." + str(t)
    
    elif len(str(t)) == 2:
        c = str(t)[0]
        d = str(t)[1]
        return "0:0" + c + "." + d
    else:
        if t % 600 == 0:
            a = str(t / 600)
            return a + ":00.0"
        else:
            a = str(t / 600)
            remain = t % 600
            b = str(remain / 100)
            remain2 = remain % 100
            c = str(remain2 / 10)
            remain3 = remain2 % 10
            d = str(remain3)
            return a + ":" + b + c + "." + d
   
# define event handlers for buttons; "Start", "Stop", "Reset"
def button_start():
    return timer.start()
    
def button_stop():
    global original_state
    if original_state == timer.is_running():
        return timer.stop()
    else:
        count()
        return timer.stop() 
    
def button_reset():
    global t, x, y
    t = 0
    x = 0
    y = 0
    return timer.stop()
   
def count():
    global x, y
    num = format(t)
    if num[5] == str(0):
        x += 1
        y += 1
        return x, y
    else:
        y += 1
        return x

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global t
    t += 1
    return t

# define draw handler
def draw_handler(canvas):
    global t, x, y
    canvas.draw_text(format(t), [130, 180], 50, "White")
    record = str(x) + "/" + str(y)
    canvas.draw_text(record, [260, 40], 40, "Aqua")
    if y == 0:
        canvas.draw_text("Success:    %", [30, 275], 25, "White")
    else:
        rate = round(float(x) / float(y), 4) * 100
        if rate == 0.0:
            zero = "Success:0" + str(rate) + "0%"
            canvas.draw_text(zero, [30, 275], 25, "Blue")
        elif rate >= 60.0:
            success_rate = "Success:" + str(rate) + "%"
            canvas.draw_text(success_rate, [30, 275], 50, "Red")
        elif rate >= 45.0:
            success_rate = "Success:" + str(rate) + "%"
            canvas.draw_text(success_rate, [30, 275], 40, "Orange")
        elif rate >= 30.0:
            success_rate = "Success:" + str(rate) + "%"
            canvas.draw_text(success_rate, [30, 275], 35, "Yellow")
        elif rate >= 15.0:
            success_rate = "Success:" + str(rate) + "%"
            canvas.draw_text(success_rate, [30, 275], 30, "Lime")       
        elif rate >= 0.0:
            success_rate = "Success:" + str(rate) + "%"
            canvas.draw_text(success_rate, [10, 250], 25, "Green")      

# create frame
frame = simplegui.create_frame("Stopwatch", 370, 350)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)

frame.set_draw_handler(draw_handler)
frame.add_button("Start", button_start, 150)
frame.add_button("Stop", button_stop, 150)
frame.add_button("Reset", button_reset, 150)
# start frame
timer.stop()
frame.start()
