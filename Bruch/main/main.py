'''
Created on 28.12.2013

@author: uhs374h
'''

from bruch.Bruch import Bruch
from random import randint
if __name__ == '__main__':
    b1=Bruch(3,4)
    b2=Bruch(3,4)+b1
    b3=3+b1+Bruch(1,4)
    b4=3/b3+3
    b4=4*b4-2-b3
    print(str(b1)+'='+str(b1.eval()))
    print(str(b2)+'='+str(b2.eval()))
    print(str(b3)+'='+str(b3.eval()))
    print(str(b4)+'='+str(b4.eval()))
    b=[]
    for x in range(0, 10000):
        z=randint(0,50)
        n=randint(1,50)
        b.append(Bruch(z,n))

#        print(str(b[x])
    for x in range(len(b)):
        print (str(b[x])+"="+str(b[x].eval()))    
pass