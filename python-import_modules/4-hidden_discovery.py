#!/usr/bin/python3
import importlib.util


def main():
    spec = importlib.util.spec_from_file_location("hid", "/tmp/hidden_4.pyc")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    names = dir(module)
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)


if __name__ == "__main__":
    main()
