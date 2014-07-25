'''
Created on 28.12.2013

@author: uhs374h
'''

from bruch.Bruch import Bruch
from random import randint
if __name__ == '__main__':
    b1=Bruch(3,4)
    b2=Bruch(3,4)+b1
    z1,z3=b1
    z2=b1.nenner
    print(z1,z2)
    b3=3+b1+Bruch(1,4)
    b4=3/b3+3
    b3+=Bruch(3,2)
    b0=Bruch(4,3)
    print(str(b1)+" == invert "+str(b0),b1== ~b0 )
    b3=-b3
    print(b3 is not b2)
    b5=Bruch(b3.zaehler,b3.nenner)
    print(b3 is b5)
    b4=4*b4-Bruch(2,4)-b3**2
    print(str(b1)+'='+str(b1.eval()))
    print(str(b2)+'='+str(b2.eval()))
    print(str(b3)+'='+str(b3.eval()))
    print(str(b4)+'='+str(b4.eval()))
    print("abs"+str(b4)+" = "+str(abs(b4)))
    b=[]
    for x in range(0, 1000):
        z=randint(0,50)
        n=randint(1,50)
        b.append(Bruch(z,n))

#        print(str(b[x])
    for x in range(len(b)):
        print (str(b[x])+"="+str(b[x].eval())
               +((", gt "+str(b1)) if (b[x]>b1) else "")
               +((", ge "+str(b1)) if (b[x]>=b1) else "")
               +((", lt "+str(b1)) if (b[x]<b1) else "")
               +((", le "+str(b1)) if (b[x]<=b1) else "")
               +((", == "+str(b1)) if (b[x]==b1) else "")
               +((", != "+str(b1)) if (b[x]!=b1) else ""))    
pass