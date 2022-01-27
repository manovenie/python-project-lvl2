from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain

FORMAT_TYPES = {
    'stylish': format_stylish,
    'plain': format_plain,
}


def get_formatter(diff, style='stylish'):
    formatter = FORMAT_TYPES.get(style)
    return formatter(diff)
