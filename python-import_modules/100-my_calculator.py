#!/usr/bin/python3
import calculator_1 as calc
import sys


def main():
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]
    result = 0
    if operator == "+":
        result = calc.add(a, b)
    elif operator == "-":
        result = calc.sub(a, b)
    elif operator == "*":
        result = calc.mul(a, b)
    elif operator == "/":
        result = calc.div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print(f"{a} {operator} {b} = {result}".format())


if __name__ == "__main__":
    main()
