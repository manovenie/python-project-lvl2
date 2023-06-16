from gendiff.status_constants import Status


ADDED_STR = "Property '{0}' was added with value: {1}"
DELETED_STR = "Property '{0}' was removed"
CHANGED_STR = "Property '{0}' was updated. From {1} to {2}"


def format_plain(diff, key_path=None):  # noqa: C901
    if key_path is None:
        key_path = []
    res = []
    for diff_key, diff_value in sorted(diff.items()):
        key_path.append(diff_key)
        status, rest = diff_value[0], diff_value[1:]
        value = rest[0]
        formatted_value = format_value(value)
        if status == Status.CHANGED.value:
            updated_value = rest[1]
            formatted_updated_value = format_value(updated_value)
            res.append(CHANGED_STR.format(
                '.'.join(key_path), formatted_value, formatted_updated_value))
        if status == Status.ADDED.value:
            res.append(ADDED_STR.format(
                '.'.join(key_path), formatted_value))
        if status == Status.DELETED.value:
            res.append(DELETED_STR.format('.'.join(key_path)))
        if status == Status.NESTED.value:
            res.append(format_plain(value, key_path))
        key_path.pop()
    return '\n'.join(res)


def format_value(value):
    if type(value) in (list, dict):
        value = '[complex value]'
    elif isinstance(value, bool):
        value = str(value).lower()
    elif value is None:
        value = 'null'
    elif isinstance(value, str):
        value = f"'{value}'"
    return value
