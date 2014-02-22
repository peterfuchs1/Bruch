'''
Created on 27.12.2013

@author: uhs374h
'''
class Bruch(object):
    '''
    classdocs
    zaehler int
    nenner int
    '''
    

    def __init__(self, zaehler,nenner=1):
        '''
        Constructor
        '''
        if isinstance(zaehler, Bruch):
            self.zaehler=zaehler.zaehler
            self.nenner=zaehler.nenner
            return
        elif type(zaehler) is not int:
            raise TypeError('incompatible type:'+type(zaehler).__name__)
        elif type(nenner) is not int:
            raise TypeError('incompatible type:'+type(nenner).__name__) 
        if nenner==0:
            raise ZeroDivisionError
        self.zaehler=zaehler
        self.nenner=nenner
            
    def __radd__(self,zaehler):
        '''
        the r-version
        '''
        return self.__add__(zaehler)

    def __add__(self,zaehler):
        '''
        overloading +
        '''
        if isinstance(zaehler, Bruch):
            z2=zaehler.zaehler
            n2=zaehler.nenner
        elif type(zaehler) is int:
            z2=zaehler
            n2=1
        else:
            raise TypeError('incompatible types:'+type(zaehler).__name__+' + Bruch()')        
        nennerNeu=self.nenner*n2
        zaehlerNeu=z2*self.nenner+n2*self.zaehler
        return Bruch(zaehlerNeu,nennerNeu)
    
    def __rsub__(self,left):
        '''
        the r-version
        '''
        if type(left) is int:
            z2=left        
            nennerNeu=self.nenner
            zaehlerNeu=z2*self.nenner-self.zaehler
            return Bruch(zaehlerNeu,nennerNeu)
        else:
            raise TypeError('incompatible types:'+type(left).__name__+' - Bruch()')
            
            
    def __sub__(self,zaehler):
        '''
        overloading -
        '''
        return self.__add__(zaehler*-1)
    def __rmul__(self,zaehler):
        '''
        the r-version
        '''
        return self.__mul__(zaehler)
    
    def __mul__(self,zaehler):
        '''
        overloading *
        '''
        if isinstance(zaehler, Bruch):
            z2=zaehler.zaehler
            n2=zaehler.nenner
        elif type(zaehler) is int:
            z2=zaehler
            n2=1
        else:
            raise TypeError('incompatible types:'+type(zaehler).__name__+' * Bruch()')
        z2*=self.zaehler
        n2*=self.nenner
        return Bruch(z2,n2)
    
    def __rtruediv__(self,left):
        '''
        the r-version
        '''
        if type(left) is int:
            z2=left*self.nenner
            if self.zaehler==0:
                raise ZeroDivisionError
            return Bruch(z2,self.zaehler)        
        else:
            raise TypeError('incompatible types:'+type(left).__name__+' / Bruch()')
        
#    def __div__(self,zaehler):
#        overloading / prior py2.1
#       return self.__truediv__(zaehler)
        
    def __truediv__(self,zaehler):
        '''
        overloading /
        '''
        if isinstance(zaehler, Bruch):
            z2=zaehler.zaehler
            n2=zaehler.nenner
        elif type(zaehler) is int:
            z2=zaehler
            n2=1
        else:
            raise TypeError('incompatible types:'+type(zaehler).__name__+' / Bruch()')
        if z2==0:
            raise ZeroDivisionError
        return self.__mul__(Bruch(n2,z2))    


    def eval(self):
        '''
        evaluate
        '''
        real=self.zaehler/self.nenner
        return real
        
    def __str__(self):
        '''
        Vor der Ausgabe wir gekuerzt!
        '''
        shorten=Bruch.gcd(self.zaehler, self.nenner)
        self.zaehler//=shorten
        self.nenner//=shorten
        if self.nenner==1:
            return "({:d})".format(self.zaehler)
        else:    
            return "({:d}/{:d})".format(self.zaehler, self.nenner)
    
    @staticmethod
    def gcd(x,y):
        '''
        Euklidscher Algorithmus
        '''
        if x<y: x,y=y,x
        if y==0: return x
        return Bruch.gcd(y,x%y) 
pass