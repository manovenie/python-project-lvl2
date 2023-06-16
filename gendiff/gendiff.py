#!/usr/bin/env python3
from gendiff.file_parser import prepare_file
from gendiff.formatters.get_format import get_formatter
from gendiff.status_constants import Status


def generate_diff(path_file1, path_file2, output_format='stylish'):
    old_file = prepare_file(path_file1)
    new_file = prepare_file(path_file2)
    diff = create_diff(old_file, new_file)
    return get_formatter(diff, output_format)


def create_diff(old_file, new_file):
    diff = {}
    added_keys = new_file.keys() - old_file.keys()
    deleted_keys = old_file.keys() - new_file.keys()
    intersection_keys = old_file.keys() & new_file.keys()
    for key in added_keys:
        diff[key] = [Status.ADDED.value, new_file.get(key)]
    for key in deleted_keys:
        diff[key] = [Status.DELETED.value, old_file.get(key)]
    for key in intersection_keys:
        diff[key] = create_intersection_diff(
            old_file.get(key), new_file.get(key))
    return diff


def create_intersection_diff(old_value, new_value):
    if isinstance(old_value, dict) and isinstance(new_value, dict):
        return [Status.NESTED.value, create_diff(old_value, new_value)]
    if old_value == new_value:
        return [Status.UNCHANGED.value, old_value]
    return [Status.CHANGED.value, old_value, new_value]
