#!/usr/bin/env python3

from gendiff.gendiff import generate_diff
from gendiff.parser import parse_cli_args
from gendiff.parser import prepare_file
from gendiff.formatters.get_format import get_formatter


def main():
    arguments = parse_cli_args()
    first_file = prepare_file(arguments.first_file)
    second_file = prepare_file(arguments.second_file)
    diff = generate_diff(first_file, second_file)
    result = get_formatter(diff, arguments.format)
    print(result)


if __name__ == '__main__':
    main()
