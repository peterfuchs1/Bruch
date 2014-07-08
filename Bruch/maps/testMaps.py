'''
Created on 06.07.2014

@author: uhs374h
'''
from maps.BetterMaps import BetterMap
import random
from time import time

if __name__ == '__main__':
    m=BetterMap()
    for i in range(100):
        m.add(i, random.randint(0,100))
    
    # test values
    tests=(random.randint(0,100) for i in range(1000))
    dt=time()
    for k in tests:
        m.get(k)
    ddif= time()-dt
    print(ddif)
    pass