#!/usr/bin/python

"""
This program implements the GNU command 'bash'
that is written by Paul Eggert

Copyright 2024 because I said so
"""

import random, sys
import string
from argparse import ArgumentParser
import argparse

def main():
    """ Add only the regular nothing argument to argparser"""
    parser = ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    parser.add_argument('file', nargs='*', help='Gets file')
    mode.add_argument('-e', '--echo', action='store_true', help='Each argument is part of the input')
    mode.add_argument('-i', '--input-range', type=str, help='Permutates from lo to hi')
    parser.add_argument('-r', '--repeat', action='store_true', help='Repeat without repalacement')
    parser.add_argument('-n', '--head-count',type=int,  help='Specify number of words printed')

    
    
    args = parser.parse_args()

    
    """For defining modes"""
    checkEcho = False;
    checkLoHi = False;

    if args.echo:
        #if(args.file or args.input_range):
            #print('''Error: Incorrect parameters
            #shuf [option]... [file]
            #shuf -e [option]... [arg]...
            #shuf -i lo-hi [option]''')
            #exit(1)
        lines = args.file
        checkEcho = True
    elif args.file:
        if(args.echo or args.input_range):
            print('''Error: Incorrect parameters
            shuf [option]... [file]
            shuf -e [option]... [arg]...
            shuf -i lo-hi [option]''')
            exit(1)
        if len(args.file) != 1:
            print("Error: Wrong files inputted")
            exit(1)
        file = args.file[0]
        if file == "-":
            lines = sys.stdin.readlines()
        else: 
            with open(file, "r") as f:
                lines = f.readlines()
        lines = [x.strip('\n') for x in lines]
    elif args.input_range:
        if(args.echo or args.file):
            print('''Error: Incorrect Parameters
            shuf [option]... [file]
            shuf -e [option]... [arg]...
            shuf -i lo-hi [option]''')
        lo, hi = map(int, args.input_range.split('-'))
        lines = list(range(lo, hi+1))
        checkLoHi = True;
    else:
        lines = sys.stdin.readlines()
        lines = [x.strip('\n') for x in lines]

    random.shuffle(lines)

    if checkEcho or checkLoHi:
        """For Echo or LoHi"""
        random.shuffle(lines)
        """For repeat"""
        if args.repeat:
            if (args.head_count != None):
                # len(lines) gives the numbers of words/numbers
                for i in range (0, args.head_count):
                    print(random.choice(lines))
            else:
                while True:
                    print(random.choice(lines))
                    """No repeat below"""
        else:
            if(args.head_count != None):
                #Some code
                if(args.head_count <= len(lines)):
                    for i in range (0, args.head_count):
                        print(lines[i])
                else:
                    for i in lines:
                        print(i)
            else:
                for i in lines:
                    print(i)
    else:
        """For regular (ie no Echo or LoHi)"""
        random.shuffle(lines)
        """For repeat"""
        if args.repeat:
            if(args.head_count != None):
                for i in range (0, args.head_count):
                    print(random.choice(lines))
            else:
                while True:
                    print(random.choice(lines))
                """No repeat below"""
        else:
            if(args.head_count != None):
                # some code
                if(args.head_count <= len(lines)):
                    for i in range (0, args.head_count):
                        print(lines[i])
                else:
                    for i in lines:
                        print(i)
            else:
                for i in lines:
                    print(i)

            
if __name__ == "__main__":
    main()
