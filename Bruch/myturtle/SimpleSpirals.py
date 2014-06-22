"""This module is part a new part of Swampy with object-oriented approach 

Copyright 2014 walter rafeiner-magor
"""

from abc import ABCMeta,abstractmethod

class SimpleSpirals(metaclass=ABCMeta):
        
    @abstractmethod
    def draw_spiral(self, n, length=3, a=0.1, b=0.0002):
	    """Draws an Archimedian spiral starting at the origin.
			Args:
			n: how many line segments to draw
			length: how long each segment is
			a: how loose the initial spiral starts out (larger is looser)
			b: how loosly coiled the spiral is (larger is looser)
			http://en.wikipedia.org/wiki/Spiral
		"""
	    pass
		
       