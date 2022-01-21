#!/usr/bin/env python3
import json


def generate_diff(file_path1, file_path2):
    x = json.load(open(file_path1))
    y = json.load(open(file_path2))
    res = '{\n'
    all_keys = sorted(list(x.keys() | y.keys()))
    intersection_keys = x.keys() & y.keys()
    deleted_keys = x.keys() - y.keys()
    added_keys = y.keys() - x.keys()
    for key in all_keys:
        if key in intersection_keys:
            if x[key] == y[key]:
                res += '    {}: {}\n'.format(key, x[key])
            else:
                res += '  - {}: {}\n'.format(key, x[key])
                res += '  + {}: {}\n'.format(key, y[key])
        elif key in deleted_keys:
            res += '  - {}: {}\n'.format(key, x[key])
        elif key in added_keys:
            res += '  + {}: {}\n'.format(key, y[key])

    res += '}'
    return res
