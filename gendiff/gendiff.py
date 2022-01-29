#!/usr/bin/env python3
from gendiff.file_parser import prepare_file
from gendiff.formatters.get_format import get_formatter
from gendiff.status_constants import (
    ADDED,
    CHANGED,
    DELETED,
    NESTED,
    UNCHANGED,
)


def create_diff(old_file, new_file):
    diff = {}
    intersection_keys = old_file.keys() & new_file.keys()
    deleted_keys = old_file.keys() - new_file.keys()
    added_keys = new_file.keys() - old_file.keys()
    for key in added_keys:
        diff[key] = [ADDED, new_file.get(key)]
    for key in deleted_keys:
        diff[key] = [DELETED, old_file.get(key)]
    for key in intersection_keys:
        old_value = old_file.get(key)
        new_value = new_file.get(key)
        has_children = isinstance(old_value, dict) and\
            isinstance(new_value, dict)
        if has_children and old_value != new_value:
            diff[key] = [NESTED, create_diff(old_value, new_value)]
        elif old_value == new_value:
            diff[key] = [UNCHANGED, old_value]
        else:
            diff[key] = [CHANGED, old_value, new_value]
    return diff


def generate_diff(path_file1, path_file2, output_format='stylish'):
    old_file = prepare_file(path_file1)
    new_file = prepare_file(path_file2)
    diff = create_diff(old_file, new_file)
    return get_formatter(diff, output_format)
