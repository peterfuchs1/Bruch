'''
Created on 11.07.2014

@author: uhs374h
'''
import csv
import sys


class GPXConversion:

    def __init__(self, inputFilename="munzee.csv", outputFilename="munzee.gpx",creator="convertpy"):
        self.inputFilename = inputFilename
        self.outputFilename = outputFilename
        self.creator=creator
        self.inputFile=None
        self.outputFile=None

    
    @staticmethod
    def conversion(old):
        direction = {'N':1.0, 'S':-1.0, 'E': 1.0, 'W':-1.0}
        new = old.replace('\'',' ')
        new = new.split()
        ret=(float(new[1])+float(new[2])/60.0) * direction[new[0]]
        return ret
    #=========================================================================
    # openFiles
    #=========================================================================
    def openFiles(self):
        if self.inputFilename == None or self.inputFilename == "-":
            self.inputFile = sys.stdin
        else:
            try:
                self.inputFile = open(self.inputFilename, "r")
            except IOError:
                strerror = sys.exc_info()
                sys.stderr.write("File: %s: not found\n" % (self.inputFilename, strerror))
                sys.exit(2)
    
        if self.outputFilename == None or self.outputFilename == "-":
            self.outputFile = sys.stdout
        else:
            try:
                self.outputFile = open(self.outputFilename, "w")
            except IOError:
                strerror = sys.exc_info()
                sys.stderr.write("Couldn't write to: %s \n" % (self.outputFilename, strerror))
                sys.exit(3)

    #=========================================================================
    # WriteGPXHeader
    #=========================================================================
    def writeGPXHeader(self):
        self.outputFile.write("<?xml version=\"1.0\"?>\n")
        self.outputFile.write("\n<gpx version=\"1.1\" creator=\"%s\">\n" % (self.creator))

    #=========================================================================
    # writeGPXFooter
    #=========================================================================
    def writeGPXFooter(self):
        self.outputFile.write("\n</gpx>\n")
    
    #=========================================================================
    # writeGPXBody
    #=========================================================================
    def writeGPXBody(self):
        # modes:
        # 
        # processing waypoint
        
        lineNum = 0
        
        fin = self.inputFile
        fout = self.outputFile
        for line in csv.reader(fin, dialect='excel'):
            lineNum+=1
            latMM, lonMM = line[0].split(';')
            lat,lon=str(GPXConversion.conversion(latMM)), str(GPXConversion.conversion(lonMM))
            
    
    
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
    md = GPXConversion("munzee.csv","munzee.gpx")
    md.openFiles()

    md.writeGPXHeader()
    md.writeGPXBody()
    md.writeGPXFooter()
    
    pass