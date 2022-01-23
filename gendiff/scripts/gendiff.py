#!/usr/bin/env python3

import argparse
from gendiff.gendiff import generate_diff
from gendiff.parser import parse_cli_args


def main():
    arguments = parse_cli_args()
    result = generate_diff(arguments.first_file, arguments.second_file)
    print(result)


if __name__ == '__main__':
    main()
