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
from myworld.SimpleShapes import SimpleShapes
from myworld.SimpleSpirals import SimpleSpirals
from myworld.SimplePies import SimplePies
from myworld.SimpleFlowers import SimpleFlowers

import math

class MyTurtle(Turtle, SimpleShapes, SimpleSpirals, SimpleFlowers, SimplePies):
        
    def move (self,length):
        """
        moves without a trace
        """
        self.pu()
        self.fd(length)
        self.pd()
        
    def rectangle(self,length, height):
        """Draws a rectangle with sides of the given length and height.
        MyTurtleWorld.py
        Returns the Turtle to the starting position and location.
        """
        for i in range(2):
            self.fd(length)
            self.lt()
            self.fd(height)
            self.lt()
        
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
    #########################
    # implement SimplePies ##
    #########################
    def _polypie(self, n, r):
        """Draws a pie divided into radial segments.
            a helper method!
            n: number of segments
            r: length of the radial spokes
        """
        angle = 360.0 / n
        for i in range(n):
            self._isosceles(r, angle/2)
            self.lt(angle)

    def _isosceles(self, r, angle):
        """Draws an icosceles triangle.
        The turtle starts and ends at the peak, facing the middle of the base.
        a helper method
        r: length of the equal legs
        angle: peak angle in degrees
        """
        y = r * math.sin(angle * math.pi / 180)

        self.rt(angle)
        self.fd(r)
        self.lt(90+angle)
        self.fd(2*y)
        self.lt(90+angle)
        self.fd(r)
        self.lt(180-angle)

    def draw_pie(self, n, r):
        """Draws a pie, then moves into position to the right.
        n: number of segments
        r: length of the radial spokes
        """
        self._polypie(n, r)
        self.pu()
        self.fd(r*2 + 10)
        self.pd()

    ############################
    # implement SimpleSpirals ##
    ############################
    def draw_spiral(self,n, length=3, a=0.1, b=0.0002):
        """Draws an Archimedian spiral starting at the origin.
        Args:
            n: how many line segments to draw
            length: how long each segment is
            a: how loose the initial spiral starts out (larger is looser)
            b: how loosly coiled the spiral is (larger is looser)
        http://en.wikipedia.org/wiki/Spiral
        """
        theta = 0.0

        for i in range(n):
            self.fd(length)
            dtheta = 1 / (a + b * theta)

            self.lt(dtheta)
            theta += dtheta
    
    ############################
    # implement SimpleFlowers ##
    ############################
    def _petal(self,r, angle):
        """Draws a petal using two arcs.
            r: radius of the arcs
            angle: angle (degrees) that subtends the arcs
        """
        for i in range(2):
            self.arc(r, angle)
            self.lt(180-angle)


    def draw_flower(self,n, r, angle):
        """Draws a flower with n petals.
            n: number of petals
            r: radius of the arcs
            angle: angle (degrees) that subtends the arcs
        """
        for i in range(n):
            self._petal(r, angle)
            self.lt(360.0/n)
    
    

if __name__ == '__main__':
    tw = TurtleWorld(interactive=True)
    tw.wait_for_user()
