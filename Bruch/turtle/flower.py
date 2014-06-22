from swampy.TurtleWorld import Turtle,TurtleWorld, fd,lt,pu,pd,die
from swampy.World import *



def square(t,steps):
    for i in range(4):
        fd(t, steps)
        lt(t)

#polygon(bob, 7, 70)

#square(bob,120)
def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)
    
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t,r):
    arc(t,r,360)
    
#circle(bob,100)



def petal(t, r, angle):
    """Draws a petal using two arcs.

    t: Turtle
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(2):
        arc(t, r, angle)
        lt(t, 180-angle)


def flower(t, n, r, angle):
    """Draws a flower with n petals.

    t: Turtle
    n: number of petals
    r: radius of the arcs
    angle: angle (degrees) that subtends the arcs
    """
    for i in range(n):
        petal(t, r, angle)
        lt(t, 360.0/n)


def move(t, length):
    """Move Turtle (t) forward (length) units without leaving a trail.
    Leaves the pen down.
    """
    pu(t)
    fd(t, length)
    pd(t)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.001

# draw a sequence of three flowers, as shown in the book.
move(bob, -100)
flower(bob, 7, 60.0, 60.0)

move(bob, 100)
flower(bob, 10, 40.0, 80.0)

move(bob, 100)
flower(bob, 20, 140.0, 20.0)

die(bob)



#arc(bob, 100, 360)
wait_for_user()
