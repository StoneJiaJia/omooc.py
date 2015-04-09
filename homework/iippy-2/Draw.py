import simplegui
import math

# intialize globals
WIDTH = 450
HEIGHT = 300
point = [100,100]


# helper function

# define event handler for mouse click, draw
def square(pos):
    global point
    point = pos
    pos = [x,y]
    point = list(pos)
   

def draw(canvas):
    canvas.draw_polygon([[x,y],[x,y+20],[x+20,y+20],[x+20,y]], 1, "Black", "Red")

# create frame
frame = simplegui.create_frame("Mouse selection", WIDTH, HEIGHT)
frame.set_canvas_background("White")

# register event handler
frame.set_mouseclick_handler(square)
frame.set_draw_handler(draw)

# start frame
frame.start()
