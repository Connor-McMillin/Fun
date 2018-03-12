#!/usr/bin/env python2

#   Last year I learned that Java accepts unicode characters in code and as a result any Java program
#   can be written solely in escaped unicode characters. This python script can take Java source code
#   and convert it into escaped unicode characters or vice versa. Both programs will compile and run
#   the exact same, just one isn't human readable.

import os
import sys
import argparse

from sys import argv

def main(fileName, conversion):
    if conversion == "1":
        toUnicode(fileName)
    else:
        toAscii(fileName)

def toUnicode(fileName):
    fin = open(fileName, "r")
    converted = ''
    
    for line in fin:
        for character in line:
            escapeChar = str(hex(ord(character))[2:])
            converted += "\u" + "0"*(4-len(escapeChar)) + escapeChar

    fin.close()

    fout = open(fileName, "w")
    fout.write(converted)
    fout.close()

def toAscii(fileName):
    fin = open(fileName, "r")
    converted = ''
   
    for line in fin:
        i = 0

        while i < len(line):
            unicodeChar = (line)[i:i+6]
            hexChar = unicodeChar[2:]
            converted += chr(int(hexChar, 16))
            i = i + 6

    fin.close()

    fout = open(fileName, "w")
    fout.write(converted)
    fout.close()

if __name__ == '__main__':
    if(len(argv) != 3):
        print "Usage: ./convert.py <fileName> <conversion type>"
        print "Where conversion type is 1 for converting to unicode and anything else to convert back"
        sys.exit(0)
    
    main(argv[1], argv[2])
