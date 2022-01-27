from gendiff.formatters.stylish import format_stylish


FORMAT_TYPES = {
    'stylish': format_stylish,
}


def get_formatter(diff, format='stylish'):
    formatter = FORMAT_TYPES.get(format)
    return formatter(diff)
