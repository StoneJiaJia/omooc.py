import math
import simplegui
message = "welcome!"
import random
t = 6000
interval = 100
secret_number = 0
value = "0"
num_range = 0
left = 7
low_number = 1
high_number = 100
i = 50
# helper function to start and restart the game
def new_game():
    global t,message,interval,secrect_number,value,left
    t = 600
    interval = 100
    secret_number = 0
    value = "0"
    num_range = 0
    left = 7
    message = "welcome!"

    
    
   
    
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
    global left
    left = 7
    secret_number = random.randrange(0, 100)
    message = "Guess the number!"
    global t
    t = 600
    timer.start() 
    new_game
    print  secret_number
    
def range1000():
    global message
    global secret_number
    global number_guess
    global left
    num_range = 1000
    left = 10
    secret_number = random.randrange(0,1000)
    message = "Guess the number!"
    global t
    t = 600
    timer.start() 
    print secret_number

def number_guess(val):
    
    global message,value,left
    value = int (val)
    

# mian game logic goes here
    
    

    if  value == secret_number:
        
        
        message = "You are right"
        new_game()

    elif value > secret_number:
        left = left -1
        message = "Lower"
        
        print i
        

    elif value < secret_number:
       
        left = left - 1
        
        message = "Higher!"
        
    
            
    else:
        message = "Invalid entry"
    if left == 0:
        message = "You lose"
        new_game()
      
#define AI guess   
def AI_guess():
    global i,value
    if i > secret_number:
        i = int((i - low_number)*0.5)
    elif i < secret_number:
        i = int((high_number - i)*0.5 + i)
        
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
    global value
    text = format(t)
    number = number_guess
   
 
    
    canvas.draw_text(str(value), (250, 250), 50, "pink")
    canvas.draw_text( str(text), (145, 100),20, "white")
    canvas.draw_text("left"+str(left), (30,40), 20, "white")
    canvas.draw_text(message, [50,70], 24, "Red")
    canvas.draw_text("AI guess "+str(i), (250, 50), 30, "Red")
        
        
        
            
# creat frame 
frame = simplegui.create_frame("Guess the number", 500,500,)
    
# register event handlers for control elements and start frame
frame.add_button("Range: [0,100)", range100, 200)
frame.add_button("Range: [0,1000)", range1000, 200)
frame.add_input("Enter a guess", number_guess, 200)
frame.add_button("AI Guess", AI_guess, 200)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)
# call new_game 
new_game()
    
    
    
    
    
    
    
    
# start frame
frame.start()
