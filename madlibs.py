#!/usr/bin/env python3

"""
File: madlibs.py
Name:

A madlibs adventure!
Concepts covered: Strings, IO, printing
"""

def main():
    # Code here
    name = input("Please enter a name: ")
    place = input("Please enter a place:")
    vehcle = input("Please enter a vehcle:")
    verb = input("Please enter an adverb:")
    adverb= input("Please enter a verb:")
    print(str(name)+ (" raced to")+ str(place)+ " by flying in her"+ str(vehcle)+ ", from which she"+ str(adverb)+ str(verb)+ " onto the campus.")
    
if __name__ == "__main__":
    main()
