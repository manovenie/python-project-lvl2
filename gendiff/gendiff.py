#!/usr/bin/env python3
import json

def generate_diff(file_path1, file_path2):
    x = json.load(open(file_path1))
    y = json.load(open(file_path2))
    res = '{\n'
    all_keys = sorted(list(x.keys() | y.keys()))
    deleted_from_file1 = x.keys() - y.keys()
    added_to_file2 = y.keys() - x.keys()
    intersection_keys = x.keys() & y.keys()
    for key in all_keys:
        if key in deleted_from_file1:
            res += '\t- {}: {}\n'.format(key, x[key])
        elif key in added_to_file2:
            res += '\t+ {}: {}\n'.format(key, y[key])
        elif key in intersection_keys:
            if x[key] == y[key]:
                res += '\t  {}: {}\n'.format(key, x[key])
            else:
                res += '\t- {}: {}\n'.format(key, x[key])
                res += '\t+ {}: {}\n'.format(key, y[key])
    res += '}\n'
    return res
