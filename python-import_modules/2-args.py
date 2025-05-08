#!/usr/bin/python3
import sys
def main():
    if len(sys.argv) == 2:
        argument = "argument"
    else:
        argument = "arguments"
    print(f"{len(sys.argv) - 1} {argument}".format())
    for i in range(1,len(sys.argv)):
        print(f"{i}: {sys.argv[i]}".format())


if __name__ == "__main__":
    main()