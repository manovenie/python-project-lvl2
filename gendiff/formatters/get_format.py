from gendiff.formatters.stylish import format_stylish


FORMAT_TYPES = {
    'stylish': format_stylish(),
}


def get_formatter(diff, format):
    style = FORMAT_TYPES.get(format)
    return style(diff)
