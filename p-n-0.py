#!/usr/bin/env python3

# Created by: Sydney Kuhn
# Created on: Sep 2020
# This program can determine if a number is positive, negative, or a zero


def main():

    # this function is the program

    # input
    integer = int(input("Enter an Integer: "))

    # process & output
    if integer > 0:
        print("{0} is a positive number.".format(integer))
    elif integer < 0:
        print("{0} is a negative number.".format(integer))
    elif integer == 0:
        print("{0} is just a zero.".format(integer))

    print("")
    print("Done.")


if __name__ == "__main__":
    main()
