#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = f"Last digit of {number} is "
comp = "and is 0"
lastdigit = number % 10
if number < 0:
    lastdigit = -1 * number % 10
    lastdigit = lastdigit * - 1
    comp = "and is less than 6 and not 0"
if lastdigit == 0:
    comp = "and is 0"
elif lastdigit > 0 and lastdigit < 6:
    comp = "and is less than 6 and not 0"
elif lastdigit > 5:
    comp = "and is greater than 5"
str = f"{str}{lastdigit} {comp}"
print(str)
