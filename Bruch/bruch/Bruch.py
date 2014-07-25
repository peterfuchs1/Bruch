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
    def __iter__(self):
        ''' make our class iterable ''' 
        self.count = 0
        self.liste = (self.zaehler,self.nenner)  
        return self

    def __next__(self):
        ''' receive the next value ''' 
        if self.count == len(self.liste):
            raise StopIteration
        self.count +=1
        return self.liste[self.count - 1]

    def __init__(self, zaehler,nenner=1):
        '''
        Constructor
        '''
        if isinstance(zaehler, Bruch):
            self.zaehler,self.nenner=zaehler
            return
        elif type(zaehler) is not int:
            raise TypeError('incompatible type:'+type(zaehler).__name__)
        elif type(nenner) is not int:
            raise TypeError('incompatible type:'+type(nenner).__name__) 
        if nenner==0:
            raise ZeroDivisionError
        self.zaehler=zaehler
        self.nenner=nenner
            
    def __neg__(self):
        ''' -Bruch '''
        return Bruch(-self.zaehler,self.nenner)
    
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
#             z2=zaehler.zaehler
#             n2=zaehler.nenner
            z2,n2=zaehler
        elif type(zaehler) is int:
#             z2=zaehler
#             n2=1
            z2,n2=zaehler,1
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
            z2,n2=zaehler
        elif type(zaehler) is int:
            z2,n2=zaehler,1
        else:
            raise TypeError('incompatible types:'+type(zaehler).__name__+' * Bruch()')
        z2*=self.zaehler
        n2*=self.nenner
        return Bruch(z2,n2)
    def __pow__(self,p):
        '''
        Bruch()^p
        '''
        if type(p) is int:
            return Bruch(self.zaehler**p,self.nenner**p)
        else:
            raise TypeError('incompatible types:'+type(p).__name__+' should be an int')
             
    
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
            z2,n2=zaehler
        elif type(zaehler) is int:
            z2,n2=zaehler,1
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
        String Repraesentation
        '''
        # Vor der Ausgabe wird gekuerzt!
        shorten=Bruch.gcd(self.zaehler, self.nenner)
        self.zaehler//=shorten
        self.nenner//=shorten
        # Nenner stehts positiv
        if self.nenner<0:
            self.nenner*=-1
            self.zaehler*=-1
            
        if self.nenner==1:
            return "({:d})".format(self.zaehler)
        else:    
            return "({:d}/{:d})".format(self.zaehler, self.nenner)
    @classmethod    
    def _makeBruch(other):
        '''create a Bruch from int or return the reference'''
        if isinstance(other, Bruch):
            return other
        elif type(other) is int:
            b=Bruch(other,1)
            return b
        else:
            raise TypeError('incompatible types:'+type(other).__name__+' not an int nor a Bruch')
    #################################
    # Overload the logical operators
    #################################    
    def __eq__ (self, other):
        '''override == '''        
        other=Bruch._makeBruch(other)
        return self.zaehler*other.nenner == other.zaehler*self.nenner
    
    def __ne__ (self, other):
        '''override !='''        
        return not self.__eq__(other)

    def __gt__ (self, other):
        '''override >'''        
        other=Bruch._makeBruch(other)
        return self.zaehler*other.nenner > other.zaehler*self.nenner
    
    def __lt__ (self, other):
        '''override <'''         
        other=Bruch._makeBruch(other)
        return self.zaehler*other.nenner < other.zaehler*self.nenner
    
    def __ge__ (self, other):
        '''override >='''        
        other=Bruch._makeBruch(other)
        return self.zaehler*other.nenner >= other.zaehler*self.nenner
    
    def __le__ (self, other):
        '''override <='''        
        other=Bruch._makeBruch(other)
        return self.zaehler*other.nenner <= other.zaehler*self.nenner

    def __abs__(self):
        '''override abs(Bruch)'''
        return Bruch(abs(self.zaehler),abs(self.nenner))
    #################################
    # Overload inplace operators
    # to raise a TypeError if necessary
    #################################
    def __iadd__(self,other):
        '''override +='''
        other=Bruch._makeBruch(other)
        self=self+other
        return self
    
    def __isub__(self,other):
        '''override -='''
        other=Bruch._makeBruch(other)
        self=self-other
        return self
    
    def __imul__(self,other):
        '''override *='''
        other=Bruch._makeBruch(other)
        self=self*other
        return self
    
    def __itruediv__(self,other):
        '''override /='''
        other=Bruch._makeBruch(other)
        self=self/other
        return self
    
    @classmethod
    def gcd(x,y):
        '''
        Euklidscher Algorithmus
        '''
        x,y=abs(x),abs(y) # positive Werte!!
        if x<y: x,y=y,x
        #Berechnung 
        while y != 0:
            x,y = y,x%y
        return x
