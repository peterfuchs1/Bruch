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
    print(b3)
    b3=-b3
    print(b3 is not b2)
    b5=Bruch(b3.zaehler,b3.nenner)
    print(b3 is b5)
    b4=4*b4-Bruch(2,4)-b3**2
    print(b1,'=',b1.eval())
    print(b2,'=',b2.eval())
    print(b3,'=',b3.eval())
    print(b4,'=',b4.eval())
    print("abs",b4,"=",abs(b4))
    b=[]
    for x in range(0, 1000):
        z=randint(0,50)
        n=randint(1,50)
        b.append(Bruch(z,n))

#        print(str(b[x])
    for x in range(len(b)):
        print (b[x],"= "+str(b[x].eval())+
               ("; gt %s" %b1 if b[x]>b1 else '')+
               ("; ge %s" %b1 if b[x]>=b1 else '')+
               ("; lt %s" %b1 if b[x]<b1 else '')+
               ("; le %s" %b1 if b[x]<=b1 else '')+
               ("; eq %s" %b1 if b[x]==b1 else '')+
               ("; ne %s" %b1 if b[x]!=b1 else ''))
        