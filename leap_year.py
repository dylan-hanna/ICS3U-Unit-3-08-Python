#!/usr/bin/env python3

# Created by: Dylan Hanna
# Created on: October 2019
# This tells you if you can date the ladies grandchild


def main():

    year_as_string = input("Enter a year: ")
    print("")

    # process & output
    try:
        year = int(year_as_string)
        if year % 4 == 0 and year % 100 != 0:
                print("It's a leap year")
        if year % 4 != 0:
            print("Not a leap year")
        if year % 4 == 0 and year % 100 == 0:
            if year % 400 != 0:
                print("It's not a leap year")
        if year % 400 == 0 and year % 100 == 0:
                        print("It is a leap year")

    except ValueError:
        print()
        print("Invalid Input")
        print()


if __name__ == "__main__":
    main()
