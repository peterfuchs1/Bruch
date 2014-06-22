"""This module is part a new part of Swampy with object-oriented approach 

Copyright 2014 walter rafeiner-magor
"""

from abc import ABCMeta,abstractmethod

class SimplePies(metaclass=ABCMeta):
        
    @abstractmethod
    def draw_pie(self, n, r):
        """Draws a pie, then moves into position to the right.
        n: number of segments
        r: length of the radial spokes
        """
        pass
     