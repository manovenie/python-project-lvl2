import os
import json
import yaml


def prepare_file(file_path):
    file_format = get_format(file_path)
    file = open_file(file_path)
    open_type = parse_file(file_format)
    return open_type(file)


def get_format(file_path):
    file_format = os.path.splitext(file_path)[1]
    return file_format


def open_file(file_path):
    with open(os.path.abspath(file_path)) as f:
        file = f.read()
    return file


def parse_file(file_format):
    load_format = {
        '.json': json.loads,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load
    }
    return load_format[file_format]
