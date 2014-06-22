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
    bob.move( -130)

# draw polypies with various number of sides
    size = 40
    bob.draw_pie(5, size)
    bob.draw_pie(6, size)
    bob.draw_pie(7, size)
    bob.draw_pie(8, size)
    bob.die()
    wait_for_user()

