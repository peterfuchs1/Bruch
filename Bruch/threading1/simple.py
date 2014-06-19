'''
Created on 19.06.2014

@author: uhs374h
'''

import time, threading 
 
class PrimzahlThread(threading.Thread): 
    def __init__(self, zahl): 
        threading.Thread.__init__(self) 
        self.Zahl = zahl 
 
    def run(self): 
        i = 2 
        starting=time.time()
        while i*i < self.Zahl: 
            if self.Zahl % i == 0: 
                print (("%d ist nicht prim, da %d = %d * %d" % self.Zahl, self.Zahl, i, self.Zahl / i)) 
                return 
            i += 1 
        print ("%d ist prim" % self.Zahl)
        dauer= time.time()-starting
        print("Dauer der Berechnung "+"{:f}".format(dauer)+" s")
meine_threads = [] 
 
while 1: 
    eingabe = input("> ") 
    if eingabe == "ende": 
        break 
 
    thread = PrimzahlThread(int(eingabe)) 
    meine_threads.append(thread) 
    thread.start() 
 
for t in meine_threads: 
    t.join()