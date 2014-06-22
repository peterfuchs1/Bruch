"""This module is part a new part of Swampy with object-oriented approach 

Copyright 2014 walter rafeiner-magor
"""

from abc import ABCMeta,abstractmethod

class SimpleFlowers(metaclass=ABCMeta):
        
    @abstractmethod
    def draw_flower(self,n, r, angle):
        """Draws a flower with n petals.
        n: number of petals
        r: radius of the arcs
        angle: angle (degrees) that subtends the arcs
        """
        pass

    