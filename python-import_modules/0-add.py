#!/usr/bin/python3
add = __import__('add_0').add


def main():
    a = 1
    b = 2
    print(f"{a} + {b} = {add(a, b)}".format())


if __name__ == "__main__":
    main()
