from swampy.TurtleWorld import Turtle,TurtleWorld, fd,lt,pu,pd,die,bk
from swampy.World import *


from time import sleep


# check if the reader has provided letters.py
from turtle.letters import *



# The following is the code for the turtle typewriter.
# it uses some features we haven't seen yet.

def teleport(t, x, y):
    """Moves the turtle to a position in absolute coordinates."""

    # This is an example of a function that breaks the layer
    # of abstraction provided by the Level 0 primitives!
    # It takes advantage of details of the implemention that
    # should probably not be considered 'public'
    t.x = x
    t.y = y
    t.redraw()


def keypress(event):
    """Handles the event when a user presses a key.

    Checks if there is a function with the right name; otherwise
    it prints an error message.
    """
    # if we're still drawing the previous letter, bail out
    if bob.busy:
        return
    else:
        bob.busy = True

    # check if the user pressed return
    if event.char in ['\n', '\r']:
        teleport(bob, -180, bob.y-size*3)
        bob.busy = False
        return
        
    # figure out which function to call, and call it
    try:
        func = eval('draw_' + event.char)
    except NameError:
        print ("I don't know how to draw an", event.char)
        bob.busy = False
        return

    func(bob, size)

    skip(bob, size/2)
    bob.busy = False


world = TurtleWorld()

# create and position the turtle
size = 20
bob = Turtle(world)
bob.delay = 0.01
bob.busy = False
teleport(bob, -180, 150)

# tell world to call keypress when the user presses a key
world.bind('<Key>', keypress)

world.mainloop()