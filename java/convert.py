#!/usr/bin/env python

import os
import sys
import argparse

from sys import argv

def main(fileName, conversion):
    file = open(fileName, "r")
    converted = ''
    
    for line in file:
        for character in line:
            converted += unicode(character)

    print converted

if __name__ == '__main__':
    if(len(argv) != 3):
        print "Usage: ./convert.py <fileName> <conversion type>"
        print "Where conversion type is 1 for converting to unicode and anything else to convert back"
        sys.exit(0)
    
    main(argv[1], argv[2])
