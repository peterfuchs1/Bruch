'''
Created on 19.06.2014

@author: uhs374h
'''

import threading 
import queue 
 
class Mathematiker(threading.Thread): 
    Ergebnis = {} 
    ErgebnisLock = threading.Lock() 
 
    Briefkasten = queue.Queue() 
 
    def run(self): 
        while True: 
            zahl = Mathematiker.Briefkasten.get() 
            ergebnis = self.istPrimzahl(zahl) 
 
            Mathematiker.ErgebnisLock.acquire() 
            Mathematiker.Ergebnis[zahl] = ergebnis 
            Mathematiker.ErgebnisLock.release() 
 
            Mathematiker.Briefkasten.task_done() 
 
    def istPrimzahl(self, zahl): 
        i = 2 
        if zahl<2:
            return "no prim"
        while i*i < zahl + 1: 
            if zahl % i == 0: 
                return "%d = %d * %d" % (zahl, zahl / i, i) 
 
            i += 1 
 
        return "prim" 
 
 
meine_threads = (Mathematiker() for i in range(5)) 
for thread in meine_threads: 
    thread.setDaemon(True) 
    thread.start() 
 
while True: 
    eingabe = input("> ") 
    if eingabe == "ende": 
        break 
    elif eingabe == "status": 
        print ("-------- Aktueller Status --------") 
        Mathematiker.ErgebnisLock.acquire() 
        for z, e in Mathematiker.Ergebnis.items(): 
            print ("%d: %s" % (z, e)) 
        Mathematiker.ErgebnisLock.release() 
        print ("----------------------------------") 
 
    elif int(eingabe) not in Mathematiker.Ergebnis: 
        Mathematiker.ErgebnisLock.acquire() 
        Mathematiker.Ergebnis[int(eingabe)] = "in Arbeit" 
        Mathematiker.ErgebnisLock.release()

        Mathematiker.Briefkasten.put(int(eingabe)) 
 
Mathematiker.Briefkasten.join()