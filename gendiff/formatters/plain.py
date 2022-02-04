from gendiff.status_constants import (
    ADDED,
    CHANGED,
    DELETED,
    NESTED,
)

ADDED_STR = "Property '{0}' was added with value: {1}"
DELETED_STR = "Property '{0}' was removed"
CHANGED_STR = "Property '{0}' was updated. From {1} to {2}"


def format_plain(diff, key_path=None):  # noqa: C901
    res = []
    if not key_path:
        key_path = []
    for key, value in sorted(diff.items()):
        key_path.append(key)
        status, rest = value[0], value[1:]
        if status == CHANGED:
            res.append(CHANGED_STR.format(
                '.'.join(key_path), format_value(rest[0]),
                format_value(rest[1])))
        elif status == ADDED:
            res.append(ADDED_STR.format(
                '.'.join(key_path), format_value(rest[0])))
        elif status == DELETED:
            res.append(DELETED_STR.format('.'.join(key_path)))
        elif status == NESTED:
            res.append(format_plain(rest[0], key_path))
        key_path.pop()
    return '\n'.join(res)


def format_value(value):
    if type(value) in (list, dict):
        return '[complex value]'
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, str):
        return f"'{value}'"
    return value
