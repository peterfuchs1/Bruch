from myworld.TurtleWorld import TurtleWorld
from myworld.World import wait_for_user
from myworld.MyTurtle import MyTurtle

# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':
    world=TurtleWorld()    
    bob=MyTurtle()
    bob.delay = 0

    bob.draw_spiral(1000)



    bob.die()
    wait_for_user()

