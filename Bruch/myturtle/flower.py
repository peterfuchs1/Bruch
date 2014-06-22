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



# draw a sequence of three flowers, as shown in the book.
    bob.move( -100)
    bob.draw_flower( 7, 60.0, 60.0)

    bob.move(100)
    bob.draw_flower(10, 40.0, 80.0)

    bob.move(100)
    bob.draw_flower(20, 140.0, 20.0)

    bob.die()
    wait_for_user()

