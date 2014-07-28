from myworld.TurtleWorld import TurtleWorld
from myworld.World import wait_for_user
from myworld.MyTurtle import MyTurtle

import math

# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':
    world=TurtleWorld()
# Wir erzeugen einen Turtle
    turty=MyTurtle()
# Der Turtle wartet auf uns
    turty.delay = 0.4

# Die Laenge betraegt 100 Punkte
    laenge = 100
    baum=laenge/2
# Wir drehen turty um 90
    turty.lt(90)
# Wir zeichen ein Quadrat
    turty.square(laenge)
# Wir gehen auf das Quadrat hinauf    
    turty.move(laenge)
# Der linke Giebel    
    turty.lt(45)
    turty.fd(laenge/2*math.sqrt(2))
# und nun der rechte Giebel    
    turty.lt(90)
    turty.fd(laenge/2*math.sqrt(2))    
# Haus ist fertig
#    turty.die()
    turty.lt(45)
    turty.move(laenge)
    turty.lt(90)
# Bitte eine Ture    
    turty.move(laenge*0.4)
    turty.rectangle(laenge*0.2,laenge*0.6)
    
# linkes Fenster
    turty.move(-laenge*0.3)
    turty.lt()
    turty.move(laenge*0.4)
    turty.lt(-90)
    turty.square(laenge*0.2)
    
# ein zweites Fenster
    turty.move(laenge*0.6)    
    turty.square(laenge*0.2)

# wir gehen nun ins Freie    
    turty.lt(-90)
    turty.move(laenge*0.4)
    turty.lt()
    turty.move(laenge)
    turty.lt(90)
# Wir zeichnen einen Baum
# Zuerst der Stamm
    turty.fd(baum)
# nun einige Aeste
    turty.lt(80)
    for x in range(0,9):
        turty.fd(baum)
        turty.move(-baum)
        turty.lt(-20)
# Der Stamm wird nun dicker
    turty.lt(-170)
    turty.fd(-3)
    turty.rectangle(6,baum)
    turty.die()
    wait_for_user()
    

