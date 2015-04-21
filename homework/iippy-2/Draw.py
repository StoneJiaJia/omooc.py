# Examples of mouse input

import simplegui
import math

# intialize globals
width = 450
height = 300
pos = []
list = []
ball_radius = 15
ball_color = "Red"
shape = 'cricle'
# helper function
def distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)
#define shape
def to_circle():
    global shape
    shape = 'cricle'

def to_square():
    global shape
    shape = 'square'
    
def to_triangle():
    global shape 
    shape = 'triangle'
    
# define event handler for mouse click, draw
def click(pos):
    list.append(pos)
      
#    if distance(ball_pos, pos) < ball_radius:
#        if ball_color == "Red":
#            ball_color = "Green"
#    else:
#        ball_pos = [pos[0], pos[1]]
#        ball_color = "Red"

def draw(canvas):
    global pos
    if shape == 'cricle':
        for ball_pos in list:
            canvas.draw_circle(ball_pos, ball_radius, 1, "Black", ball_color)
            
    if shape == 'square':
        for pos in list:
            canvas.draw_polygon([[pos[0], pos[1]], [pos[0], pos[1]+20], [pos[0]+20, pos[1]+20], [pos[0]+20, pos[1]], [pos[0],pos[1]]], 2, 'Black', 'White')
    if shape == 'triangle':
        for pos in list:
            canvas.draw_polygon([[pos[0], pos[1]],[pos[0]-15,pos[1]+30],[pos[0]+15, pos[1]+30],[pos[0],pos[1]]], 2,'Black','White')
    
# create frame
frame = simplegui.create_frame("Mouse selection", width, height)
frame.set_canvas_background("White")

# register event handler
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)
frame.add_button('cricle', to_circle, 100)
frame.add_button('square', to_square, 100)
frame.add_button('triangle', to_triangle, 100)

# start frame
frame.start()
    
