#!/usr/bin/env python3

from gendiff.cli_parser import parse_cli_args
from gendiff.gendiff import generate_diff


def main():
    arguments = parse_cli_args()
    diff = generate_diff(
        arguments.first_file, arguments.second_file, arguments.format)
    print(diff)


if __name__ == '__main__':
    main()
