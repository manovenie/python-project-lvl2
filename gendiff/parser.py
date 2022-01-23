import argparse
import os
import json
import yaml


def parse_cli_args():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', metavar='first_file', type=str)
    parser.add_argument('second_file', metavar='second_file', type=str)
    parser.add_argument(
        '-f',
        '--format',
        action='store',
        help='set format of output',
    )
    return parser.parse_args()


def prepare_file(file_path):
    file_format = get_format(file_path)
    file = open_file(file_path)
    open_type = parser(file_format)
    return open_type(file)


def get_format(file_path):
    file_format = os.path.splitext(file_path)[1]
    return file_format


def open_file(file_path):
    with open(os.path.abspath(file_path)) as f:
        file = f.read()
    return file

def parse_file(file_format):
    format = {
        '.json': json.loads,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load
    }
    return format[file_format.lower()]

