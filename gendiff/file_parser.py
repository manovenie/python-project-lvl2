import os
import json
import yaml
from json.decoder import JSONDecodeError
from yaml.scanner import ScannerError


YAML_ERROR_MSG = '{0} - incorrect YAML file'
JSON_ERROR_MSG = '{0} - incorrect JSON file'


def prepare_file(file_path):
    file_format = get_format(file_path)
    file = open_file(file_path)
    open_type = parse_file(file_format)
    try:
        return open_type(file)
    except ScannerError:
        raise YAML_ERROR_MSG.format(file_path)
    except JSONDecodeError:
        raise JSON_ERROR_MSG.format(file_path)


def get_format(file_path):
    return os.path.splitext(file_path)[1]


def open_file(file_path):
    with open(os.path.abspath(file_path)) as f:
        file = f.read()
    return file


def parse_file(file_format):
    load_format = {
        '.json': json.loads,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load,
    }
    return load_format.get(file_format)
