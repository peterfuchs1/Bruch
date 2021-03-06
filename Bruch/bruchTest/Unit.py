'''
Created on 27.12.2013

@author: uhs374h
'''
import unittest
#import bruch.Bruch import Bruch
#from bruch.Bruch import Bruch
from Bruch.bruch.Bruch import Bruch
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
        assert(float(self.b)==0.375)

    def testmal(self):
        self.b=self.b*Bruch(4)
        assert(float(self.b)==6)

    def testplus(self):
        self.b=self.b+Bruch(4,5)
        assert(float(self.b)==2.3)

    def testminus(self):
        self.b=self.b-Bruch(4,5)
        assert(float(self.b)==0.7)


    def testdiv2(self):
        self.b=self.b/self.b3
        assert(float(self.b)==0.75)

    def testmal2(self):
        self.b=self.b*self.b2
        assert(float(self.b)==2.25)

    def testplus2(self):
        self.b=self.b+self.b3
        assert(float(self.b)==3.5)

    def testminus2(self):
        self.b=self.b-self.b3
        assert(float(self.b)==-0.5)

    def testplus3(self):
        self.b2=self.b+3
        assert(float(self.b2)==4.5)

    def testminus3(self):
        self.b2=self.b-Bruch(1)
        assert(float(self.b2)==0.5)
    
    def testmal3(self):
        self.b2=self.b*2
        assert(float(self.b2)==3)
        
    def testdiv3(self):
        self.b2=self.b/2
        assert(float(self.b2)==0.75)
        
    def teststr(self):
        str1="(3/2)"
        assert(str(self.b)==str1)
        
    def teststr2(self):
        b2=Bruch(-3,-2) 
        str1="(3/2)"
        assert(str(b2)==str1)
 
    def testradd(self):
        self.b2=3+Bruch(3,2)
        assert(float(self.b2)==4.5)

    def testrmal(self):
        self.b2=2*Bruch(3,2)
        assert(float(self.b2)==3)
        
    def testrsub(self):
        self.b2=3-Bruch(3,2)
        assert(float(self.b2)==1.5)

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
        assert(float(self.b2)==1)

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
    
    def testPow(self):
        h=4
        assert(self.b2**h==Bruch(self.b2.zaehler**h,self.b2.nenner**h))
        
    def testPowError1(self):
        self.assertRaises(TypeError, self.b2.__pow__,2.0)

    def testPowError2(self):
        self.assertRaises(TypeError, self.b2.__pow__,"other")

    
    def testEqual(self):
        assert(self.b==self.b2)
    
    def testNotEqual(self):
        assert(self.b!=self.b3)
        
    def testGE(self):
        assert(self.b>=self.b2)

    def testLE(self):
        assert(self.b<=self.b2)
        
    def testLT(self):
        assert(self.b<self.b3)
    
    def testGT(self):
        assert(self.b3>self.b2)
    
    def test_makeBruchTypeError(self):
        self.assertRaises(TypeError, Bruch._Bruch__makeBruch,"other")

    def test_makeBruchInt(self):
        value=3
        b4=Bruch._Bruch__makeBruch(value)
        assert(b4.zaehler==value)

    def testAbs(self):
        b4=Bruch(-3,2)
        assert(abs(b4)==Bruch(3,2))

    def testNeg(self):
        b4=Bruch(-3,2)
        assert(-b4==Bruch(3,2))
        
    # test of references
    def testRef(self):
        assert(self.b is not self.b2)
        
    def testRef2(self):
        b4=self.b
        assert(self.b is b4)
        

    # test of inplace operators    
    def testiAdd(self):
        self.b+=1
        assert(self.b==Bruch(5,2))
    
    def testiAdd2(self):
        self.b+=Bruch(1)
        assert(self.b==Bruch(5,2))

    def testiSub(self):
        self.b-=2
        assert(self.b==Bruch(-1,2))
    
    def testiSub2(self):
        self.b-=Bruch(2)
        assert(self.b==Bruch(-1,2))

    def testiMul(self):
        self.b*=2
        assert(self.b==3)
    
    def testiMul2(self):
        self.b*=Bruch(2)
        assert(self.b==3)

    def testiDiv(self):
        self.b/=2
        assert(self.b==Bruch(3,4))
    
    def testiDiv2(self):
        self.b/=Bruch(2)
        assert(self.b==Bruch(3,4))


    def testiAddError(self):
        self.assertRaises(TypeError, self.b.__iadd__,"other")

    def testiSubError(self):
        self.assertRaises(TypeError, self.b.__isub__,"other")

    def testiMulError(self):
        self.assertRaises(TypeError, self.b.__imul__,"other")
        
    def testiDivError(self):
        self.assertRaises(TypeError, self.b.__itruediv__,"other")

    def testFloat(self):
        b=Bruch(3,4)
        assert(float(b)==0.75)

    def testInt(self):
        b=Bruch(5,4)
        assert(int(b)==1)

    def testComplex(self):
        b=Bruch(3,4)
        assert(complex(b)==0.75)

    def testInvert(self):
        z,n=5,4
        b=Bruch(z,n)
        assert(~b==Bruch(n,z))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()