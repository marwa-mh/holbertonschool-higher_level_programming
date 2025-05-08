#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if (i % 3 == 0):
            if (i % 5 == 0):
                print("FizzBuzz".format(), end=" ")
            else:
                print("Fizz".format(), end=" ")
        elif (i % 5 == 0):
            print("Buzz".format(), end=" ")
        else:
            print(f"{i}".format(), end=" ")
