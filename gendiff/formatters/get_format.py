from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish

FORMAT_TYPES = {
    'stylish': format_stylish,
    'plain': format_plain,
    'json': format_json,
}


def get_formatter(diff, style='stylish'):
    formatter = FORMAT_TYPES.get(style)
    return formatter(diff)
