"""This module is part a new part of Swampy with object-oriented approach 

Copyright 2014 walter rafeiner-magor
"""

from abc import ABCMeta,abstractmethod

class SimpleShapes(metaclass=ABCMeta):
    @abstractmethod
    def move(self, length):
        pass
        """Move Turtle forward (length) units without leaving a trail.
            Leaves the pen down.
        """

    @abstractmethod
    def rectangle(self,length, heigth):
        pass
    @abstractmethod    
    def square(self,length):
        pass
        """Draws a square with sides of the given length.
        MyTurtleWorld.pyReturns the Turtle to the starting position and location.
        """
    
    @abstractmethod    
    def polyline(self,n, length, angle):
        pass
        """Draws n line segments.
        t: Turtle object
        n: number of line segments
        length: length of each segment
        angle: degrees between segments
        """
        
    @abstractmethod
    def polygon(self,t, n, length):
        pass
        """Draws a polygon with n sides.
        t: Turtle
        n: number of sides
        length: length of each side.
        """
        
    @abstractmethod
    def arc(self,r, angle):
        pass
        """Draws an arc with the given radius and angle.
        t: Turtle
        r: radius
        angle: angle subtended by the arc, in degrees
        """
        
    @abstractmethod
    def circle(self,r):
        pass
        """Draws a circle with the given radius.
        t: Turtle
        r: radius
        """
        
