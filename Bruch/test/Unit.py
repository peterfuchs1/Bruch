'''
Created on 27.12.2013

@author: uhs374h
'''
import unittest
from bruch.Bruch import Bruch

class Test(unittest.TestCase):


    def setUp(self):
        self.b=Bruch(3,2)
        self.b2=Bruch(self.b)
        self.b3=Bruch(4,2)
        pass

    def tearDown(self):
        del self.b,self.b2,self.b3
        pass

    def testdiv(self):
        self.b=self.b/Bruch(4)
        assert(self.b.eval()==0.375)

    def testmal(self):
        self.b=self.b*Bruch(4)
        assert(self.b.eval()==6)

    def testplus(self):
        self.b=self.b+Bruch(4,5)
        assert(self.b.eval()==2.3)

    def testminus(self):
        self.b=self.b-Bruch(4,5)
        assert(self.b.eval()==0.7)


    def testdiv2(self):
        self.b=self.b/self.b3
        assert(self.b.eval()==0.75)

    def testmal2(self):
        self.b=self.b*self.b2
        assert(self.b.eval()==2.25)

    def testplus2(self):
        self.b=self.b+self.b3
        assert(self.b.eval()==3.5)

    def testminus2(self):
        self.b=self.b-self.b3
        assert(self.b.eval()==-0.5)

    def testplus3(self):
        self.b2=self.b+3
        assert(self.b2.eval()==4.5)

    def testminus3(self):
        self.b2=self.b-Bruch(1)
        assert(self.b2.eval()==0.5)
    
    def testmal3(self):
        self.b2=self.b*2
        assert(self.b2.eval()==3)
        
    def testdiv3(self):
        self.b2=self.b/2
        assert(self.b2.eval()==0.75)
        
    def teststr(self):
        str1="(3/2)"
        assert(str(self.b)==str1)
        
    def testradd(self):
        self.b2=3+Bruch(3,2)
        assert(self.b2.eval()==4.5)

    def testrmal(self):
        self.b2=2*Bruch(3,2)
        assert(self.b2.eval()==3)
        
    def testrsub(self):
        self.b2=3-Bruch(3,2)
        assert(self.b2.eval()==1.5)

    def testrdivError(self):
#        self.b2=32.0/self.b2
        self.assertRaises(TypeError, self.b2.__rtruediv__,3.0)
#        TypeError!!!

    def testrsubError(self):
#        self.b2=2.0-self.b2
        self.assertRaises(TypeError, self.b2.__rsub__,2.0)
#        TypeError!!!

    def testrdiv(self):
        self.b2=2/Bruch(2)
        assert(self.b2.eval()==1)

    def testmulError(self):
#        self.b2=2.0*Bruch(2)
        self.assertRaises(TypeError, self.b2.__mul__,2.0)

    def testaddError(self):
#        self.b2=2.0*Bruch(2)
        self.assertRaises(TypeError, self.b2.__add__,2.0)

    def testdivZeroError(self):
#        self.b2=2.0*Bruch(2)
        self.assertRaises(ZeroDivisionError, self.b2.__truediv__,0)

    def testdivTypeError(self):
#        self.b2=2.0*Bruch(2)
        self.assertRaises(TypeError, self.b2.__truediv__,3.1)


    def testdivZeroError2(self):
#        self.b2=2.0*Bruch(2)
        self.assertRaises(ZeroDivisionError, self.b2.__truediv__,Bruch(0,3))        

    def testrdivZeroError(self):
        bneu=Bruch(0,3)
        self.assertRaises(ZeroDivisionError, bneu.__rtruediv__,3)
        
    def testcreateBruchZeroError(self):
        self.assertRaises(ZeroDivisionError, Bruch,3,0)
    
    def testcreateBruchWrongTypeNenner(self):
        self.assertRaises(TypeError, Bruch,3,1.1)

    def testcreateBruchWrongTypeZaehler(self):
        self.assertRaises(TypeError, Bruch,2.0)

    def testInteger(self):
        self.b2=Bruch(3,1)
        assert(str(self.b2)=='(3)')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()