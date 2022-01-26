#!/usr/bin/env python3
from gendiff.formatters.get_format import get_formatter
from gendiff.status_constants import (
    ADDED,
    CHANGED,
    DELETED,
    NESTED,
    UNCHANGED,
)


def generate_diff(old_file, new_file, format='stylish'):
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
        if has_children:
            diff[key] = [NESTED, generate_diff(old_value, new_value)]
        elif old_value == new_value:
            diff[key] = [UNCHANGED, old_value]
        else:
            diff[key] = [CHANGED, old_value, new_value]
    return get_formatter(diff, format)
