import os
import json
import yaml
from json.decoder import JSONDecodeError
from yaml.scanner import ScannerError


EXT_ERROR_MSG = '{0} - invalid file extension\nUse one of: .json .yaml .yml'
YAML_ERROR_MSG = '{0} - incorrect YAML file'
JSON_ERROR_MSG = '{0} - incorrect JSON file'
OS_ERROR_MSG = '{0} - file access error'


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
    except OSError:
        raise OS_ERROR_MSG.format(file_path)


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
    return load_format.get(file_format)
