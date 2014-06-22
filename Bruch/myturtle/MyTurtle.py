"""This module is part a new part of Swampy with object-oriented approach 

Copyright 2014 walter rafeiner-magor
swarmy
Copyright 2010 Allen B. Downey
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""

from tkinter import TOP, BOTTOM, LEFT, RIGHT, END, LAST, NONE, SUNKEN

from myworld.Gui import Callable
from myworld.World import World, Animal, wait_for_user

from myworld.TurtleWorld import TurtleWorld, Turtle, TurtleControl

import math

class MyTurtle(Turtle):
    def square(self,length):
        """Draws a square with sides of the given length.

    MyTurtleWorld.pyReturns the Turtle to the starting position and location.
    """
        for i in range(4):
            self.fd(length)
            self.lt()
            


    def polyline(self,n, length, angle):
        """Draws n line segments.

        t: Turtle object
        n: number of line segments
        length: length of each segment
        angle: degrees between segments
        """
        for i in range(n):
            self.fd(length)
            self.lt(angle)


    def polygon(self,t, n, length):

        """Draws a polygon with n sides.

        t: Turtle
        n: number of sides
        length: length of each side.
        """
        angle = 360.0/n
        self.polyline(n, length, angle)


    def arc(self,r, angle):
        """Draws an arc with the given radius and angle.
    
        t: Turtle
        r: radius
        angle: angle subtended by the arc, in degrees
        """
    
        arc_length = 2 * math.pi * r * abs(angle) / 360
        n = int(arc_length / 4) + 1
        step_length = arc_length / n
        step_angle = float(angle) / n

        # making a slight left turn before starting reduces
        # the error caused by the linear approximation of the arc
        self.lt(step_angle/2)
        self.polyline(n, step_length, step_angle)
        self.rt(step_angle/2)


    def circle(self,r):
        """Draws a circle with the given radius.

        t: Turtle
        r: radius
        """
        self.arc(r, 360)
    

if __name__ == '__main__':
    tw = TurtleWorld(interactive=True)
    tw.wait_for_user()
