#!/usr/bin/python3
import sys


def main():
    sep = ":"
    if len(sys.argv) == 2:
        argument = "argument"
    else:
        argument = "arguments"
    if len(sys.argv) == 1:
        sep = "."
    print(f"{len(sys.argv) - 1} {argument}{sep}".format())
    for i in range(1, len(sys.argv)):
        print(f"{i}: {sys.argv[i]}".format())


if __name__ == "__main__":
    main()
