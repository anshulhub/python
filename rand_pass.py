#!/usr/bin/python3
# Created by Sam Ebison ( https://github.com/ebsa491 )
# If you have found any important bug or vulnerability,
# contact me pls ( email: ebsa491@gmail.com )

import sys
import argparse
import random
import string

GREEN_COLOR = "\033[1;32m"
NO_COLOR = "\033[0m"

def main():
    print(f"{GREEN_COLOR}{generate(args.size)}{NO_COLOR}")

def generate(size):
    return ''.join(random.choice("@!_^$" + string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(size))

if __name__ == '__main__':
    global args # The program arguments

    parser = argparse.ArgumentParser(description="Password Generator")

    # -s | --size SIZE
    parser.add_argument(
        '-s',
        '--size',
        metavar='size',
        type=int,
        default=16,
        help='the size of the password (default=16)'
    )

    args = parser.parse_args()

    main()
