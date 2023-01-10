#!/usr/bin/python3
def read_file(filename=""):
    with open(filename) as f:
        text = f.read()
        print(text, end="")
