# 3/usr/bin/env python3
# Created by Larry Nkengbeza
# Created on November 2020
# This program calculates addition

def main():
    # this program calculates addition

    # Input
    numbera = int(input("Enter the first  number to be calculated:"))
    numberb = int(input("Enter the  second number to be calculated:"))

    # Process
    addition = numbera+numberb

    # Output
    print("")
    print("{0} + {1} = {2}".format(numbera, numberb, addition))


if __name__ == "__main__":
    main()
