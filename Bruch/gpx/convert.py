'''
Created on 11.07.2014

@author: uhs374h
'''
import csv
#from math import *

#import os
import sys
#import re
#import string
#import time

class Metadata:

    def __init__(self, inputFilename="munzee.csv", outputFilename="munzee.gpx",creator="convertpy"):
        self.inputFilename = inputFilename
        self.outputFilename = outputFilename
        self.creator=creator


    

def conversion(old):
    direction = {'N':1.0, 'S':-1.0, 'E': 1.0, 'W':-1.0}
    new = old.replace('\'',' ')
    new = new.split()
    ret=(float(new[1])+float(new[2])/60.0) * direction[new[0]]
    return ret
#=========================================================================
# OpenFiles
#=========================================================================
def OpenFiles(md):
    if md.inputFilename == None or md.inputFilename == "-":
        md.inputFile = sys.stdin
    else:
        try:
            md.inputFile = open(md.inputFilename, "r")
        except IOError:
            strerror = sys.exc_info()
            sys.stderr.write("File: %s: not found\n" % (md.inputFilename, strerror))
            sys.exit(2)

    if md.outputFilename == None or md.outputFilename == "-":
        md.outputFile = sys.stdout
    else:
        try:
            md.outputFile = open(md.outputFilename, "w")
        except IOError:
            strerror = sys.exc_info()
            sys.stderr.write("Couldn't write to: %s \n" % (md.outputFilename, strerror))
            sys.exit(3)

#=========================================================================
# WriteGPXHeader
#=========================================================================
def WriteGPXHeader(md):
    fout = md.outputFile
    fout.write("<?xml version=\"1.0\"?>\n")
    fout.write("\n<gpx version=\"1.1\" creator=\"%s\">\n" % (md.creator))

#=========================================================================
# WriteGPXFooter
#=========================================================================
def WriteGPXFooter(md):
    fout = md.outputFile
    fout.write("\n</gpx>\n")
    
#=========================================================================
# WriteGPXBody
#=========================================================================
def WriteGPXBody(md):
    # modes:
    # 0 - nostate
    # 1 - processing waypoint
    # 2 - processing routes
    lineNum = 0
    
    fin = md.inputFile
    fout = md.outputFile
    for line in csv.reader(fin, dialect='excel'):
        lineNum+=1
        latMM, lonMM = line[0].split(';')
        lat,lon=str(conversion(latMM)), str(conversion(lonMM))
        


        name = "munzee"+str(lineNum).zfill(3)
        sym = "Dot"
        ele = None
        lat = lat.strip()
        lon = lon.strip()

        fout.write("\n<wpt lat=\"%s\" lon=\"%s\"" % (lat, lon))
        if any((name != None,sym != None, ele != None)):
            fout.write(">\n");
            if name != None:
                fout.write("    <name>%s</name>\n" % (name))
            if sym != None:
                fout.write("    <sym>%s</sym>\n" % (sym))
            if ele != None:
                fout.write("    <ele>%s</ele>\n" % (ele))
            fout.write("</wpt>\n")
        else:
            fout.write("/>\n")

        
        
        print ("Lat=%s Lon=%s Name:%s Sym:%s " % (lat,lon,name,sym))


if __name__ == '__main__':
    md = Metadata("munzee.csv","munzee.gpx")
    OpenFiles(md)

    WriteGPXHeader(md)
    WriteGPXBody(md)
    WriteGPXFooter(md)
    
    pass