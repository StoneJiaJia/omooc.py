# Examples of mouse input

import simplegui
import math

# intialize globals
width = 450
height = 300
pos_list = []
list = [(1000,1000)]
ball_radius = 15
ball_color = "Red"
shape = 'cricle'
i = 0
shape_list = []
# helper function

#define shape


def to_circle():
    global cricle_list
    shape = 'cricle'
    

def to_square():
    global shape
    shape = 'square'
    
def to_triangle():
    global shape 
    shape = 'triangle'
    
# define event handler for mouse click, draw
def click(pos):
    global pos_list
    list.append(pos)
    pos_list.append(pos)
     
    shape_list.append(shape)
    
      
#    if distance(ball_pos, pos) < ball_radius:
#        if ball_color == "Red":
#            ball_color = "Green"
#    else:
#        ball_pos = [pos[0], pos[1]]
#        ball_color = "Red"

def draw(canvas):
    i = 0
    while i < len(pos_list):
        if shape_list[i] == 'circle': # first use "=" instead, a "classic" error
            canvas.draw_circle(pos_list[i], 20, 2, 'Blue')
            print pos_list[i]
        elif shape_list[i] == 'triangle':
            canvas.draw_polygon([(pos_list[i][0],pos_list[i][1] + 20),
                                (pos_list[i][0] + 10,pos_list[i][1] - 10),
                                (pos_list[i][0] - 10,pos_list[i][1] - 10)],
                                2, 'Blue')
        else: # i.e.: shape_list == "square" 
            canvas.draw_polygon([(pos_list[i][0] - 15,pos_list[i][1] + 15),
                                (pos_list[i][0] + 15,pos_list[i][1] + 15),
                                (pos_list[i][0] + 15,pos_list[i][1] - 15),
                                (pos_list[i][0] - 15,pos_list[i][1] - 15)],
                                2, 'Blue')
        i += 1
   
    
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
    
