from gendiff.status_constants import Status

DEFAULT_INDENT = 4
STATUS_INDENT = 2
STATUSES = {
    'added': '+',
    'deleted': '-',
    'unchanged': ' ',
    'nested': ' ',
}


def format_stylish(diff, depth=0):  # noqa: C901
    indent = depth * DEFAULT_INDENT * ' '
    next_depth = depth + 1
    res = []
    for key, value in sorted(diff.items()):
        if isinstance(value, list):
            status, *rest = value
            if status == Status.CHANGED.value:
                res.append(generate_string('deleted', key, rest[0], next_depth))
                res.append(generate_string('added', key, rest[1], next_depth))
                continue
            res.append(generate_string(status, key, rest[0], next_depth))
            continue
        res.append(generate_string('unchanged', key, value, next_depth))
    return '{\n' + '\n'.join(res) + '\n' + indent + '}'


def generate_string(status, key, value, depth):
    indent = (depth * DEFAULT_INDENT - STATUS_INDENT) * ' '
    if isinstance(value, dict):
        result = format_stylish(value, depth)
        return f'{indent}{STATUSES[status]} {key}: {result}'
    return f'{indent}{STATUSES[status]} {key}: {format_value(value)}'


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value
