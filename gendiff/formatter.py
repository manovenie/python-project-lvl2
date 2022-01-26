from gendiff.status_constants import (
    ADDED,
    CHANGED,
    DELETED,
    NESTED,
    UNCHANGED,
)

DEFAULT_INDENT = 4
STATUS_INDENT = 2
FORMAT_TYPES = {
    'stylish': format_stylish,
}
FLAGS = {
        ADDED: '+',
        DELETED: '-',
        UNCHANGED: ' ',
    }

def get_formatter(diff, format):
    style = FORMAT_TYPES.get(format)
    return style(diff)


def format_stylish(diff, depth=0):
    indent = depth * DEFAULT_INDENT * ' '
    diff = []
    for key, value in sorted(diff.items()):
        if instance(value, list):
            status, *rest = value
            if status == DELETED:
                diff.append()


    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)

        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for key, val in current_value.items():
            lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(value, 0)

def generate_string(flag, key, value, depth):
    indent = (level * DEFAULT_INDENT - STATUS_INDENT) * ' '
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
