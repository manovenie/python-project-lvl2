from gendiff.status_constants import (
    ADDED,
    CHANGED,
    DELETED,
    NESTED,
    UNCHANGED,
)

DEFAULT_INDENT = 4
STATUS_INDENT = 2

FLAGS = {
        ADDED: '+',
        DELETED: '-',
        UNCHANGED: ' ',
    }


def format_stylish(diff, depth=0):
    indent = depth * DEFAULT_INDENT * ' '
    output = []
    for key, value in sorted(diff.items()):
        if instance(value, list):
            status, *rest = value
            if status == DELETED:
                output.append(generate_string(DELETED, key, rest[0], depth + 1))
            elif status == ADDED:
                output.append(generate_string(ADDED, key, rest[0], depth + 1))
            elif status == CHANGED:
                output.append(generate_string(DELETED, key, rest[0], depth + 1))
                output.append(generate_string(ADDED, key, rest[1], depth + 1))
            elif status == NESTED or status == UNCHANGED:
                output.append(generate_string(UNCHANGED, key, rest[0], depth + 1))
        else:
            output.append(generate_string(UNCHANGED, key, value, depth + 1))
    return '{\n' + '\n'.join(output) + '\n' + indent + '}'


def generate_string(flag, key, value, depth):
    indent = (depth * DEFAULT_INDENT - STATUS_INDENT) * ' '
    if isinstance(value, dict):
        result = format_stylish(value, depth)
        return f'{indent}{FLAGS[flag]} {key}: {result}'
    return f'{indent}{FLAGS[flag]} {key}: {format_value(value)}'


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value
