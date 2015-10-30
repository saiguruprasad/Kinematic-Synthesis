# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 13:44:43 2015

@author: balasai
"""

import getopt, sys

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print.str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    output = None
    verbose = False
    for o, a in opts:
        if o == "-v":
            verbose = True
            return verbose
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-o", "--output"):
            output = a
            return output
        else:
            assert False, "unhandled option"
    
def usage():
    print("abcd")
if __name__ == "__main__":
    main()