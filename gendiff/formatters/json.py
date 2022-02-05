import json


def format_json(diff):
    return json.dumps(sort_difference(diff))
