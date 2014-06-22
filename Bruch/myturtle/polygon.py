from myworld.TurtleWorld import TurtleWorld
from myworld.World import wait_for_user
from myworld.MyTurtle import MyTurtle

# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':
    world=TurtleWorld()    
    bob=MyTurtle()
    bob.delay = 0.001

    # draw a circle centered on the origin
    radius = 100
    #bob.pu()
    bob.fd(radius)
    bob.lt()
    #bob.pd
    bob.square(radius)
    bob.circle(radius)
    bob.die()
    wait_for_user()
    

