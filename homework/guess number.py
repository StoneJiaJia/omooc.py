
import math
import simplegui
message = "welcome!"
import random
t = 60
interval = 100
secret_number = 0
value = 0
num_range = 0
number_guess = 7
# helper function to start and restart the game
def new_game():
    t == 60
    if num_range == 100:
        range100()
    elif num_range == 1000:
        range1000()

# global variables

# in tenths of seconds into formatted string A:BC.D
def format(t):
    D = (t) % 10
    C = int(t / 10) % 10
    A = int(t / 600) % 600
    B = int(t / 100) % 6
    string = str(A) + ":" + str(B) +str(C) + "." + str(D)
    return string
    pass
# define event handlers for control panel
def range100():
    global message
    global secret_number
    global number_guess
    number_guess = 7
    secret_number = random.randrange(0, 100)
    message = "Guess the number!"
    global t
    t = 60
    timer.start() 
    
def range1000():
    global message
    global secret_number
    global number_guess
    num_range = 1000
    number_guess = 10
    secret_number = random.randrange(0,1000)
    message = "Guess the number!"
    global t
    t = 60
    timer.start() 
def input_guess(guess):
    global value
    value = int(guess)
def outcome(a):
    result = str(a)
    return result
def number_guess():
    
    if range100:
        number_guess == 7
    if range1000:
        number_guess == 10
        return number_guess
# Convert to strings

# define event handlers for buttons 

# mian game logic goes here

    if str.isdigit(outcome):
        global message
        message = "you guess is"

    if int(outcome) == secret_number:
        
        message = "You are right"
        new_game()

    if int(outcome) > secret_number:
        number_guess = number_guess - 1
        
        message = "Lower"
        if number_guess == 0:
            message = "lose"

    if int(outcome) < secret_number:
        number_guess = number_guess - 1
        message = "Higher!"
        if number_guess == 0:
            message = "You lose"
            new_game()
       
            
    else:
        message = "Invalid entry. Please enter an in-range number"

        
        
# define event handler for timer with 0.1 sec interval
def tick():
    global t
    global message
    t -= 1
    if t == 0:
        message = "Timeout"
        timer.stop()
        new_game()

# define draw handler
def draw(canvas):
    text = format(t)
    number = number_guess
   
 
    
    canvas.draw_text(outcome(value), (125, 125), 45, "pink")
    canvas.draw_text( str(text), (145, 40), 42, "white")
    canvas.draw_text("left"+str(number_guess), (30,40), 42, "white")
    canvas.draw_text(message, [50,70], 24, "Red")
   
        
        
        
        
        
        
            
# creat frame 
frame = simplegui.create_frame("Guess the number", 250,250,)
    
# register event handlers for control elements and start frame
frame.add_button("Range: [0,100)", range100, 200)
frame.add_button("Range: [0,1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)
# call new_game 
new_game()
    
    
    
    
    
    
    
    
# start frame
frame.start()

    
   
