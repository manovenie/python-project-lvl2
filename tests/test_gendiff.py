from gendiff.gendiff import generate_diff
from gendiff.formatters.get_format import format_stylish
from gendiff.formatters.plain import format_plain
from pathlib import Path
from gendiff.parser import prepare_file


def test_stylish_json():
    base_path = Path(__file__).parent
    file_path = (base_path / "../tests/fixtures/result_stylish.txt").resolve()
    file1 = prepare_file('tests/fixtures/file1.json')
    file2 = prepare_file('tests/fixtures/file2.json')
    diff = generate_diff(file1, file2)
    output = format_stylish(diff)
    with open(file_path, 'r') as result:
        assert output == result.read()
        assert isinstance(output, str)


def test_stylish_yaml():
    base_path = Path(__file__).parent
    file_path = (base_path / "../tests/fixtures/result_stylish.txt").resolve()
    file1 = prepare_file('tests/fixtures/file1.yaml')
    file2 = prepare_file('tests/fixtures/file2.yaml')
    diff = generate_diff(file1, file2)
    output = format_stylish(diff)
    with open(file_path, 'r') as result:
        assert output == result.read()
        assert isinstance(output, str)


def test_plain_json():
    base_path = Path(__file__).parent
    file_path = (base_path / "../tests/fixtures/result_plain.txt").resolve()
    file1 = prepare_file('tests/fixtures/file1.json')
    file2 = prepare_file('tests/fixtures/file2.json')
    diff = generate_diff(file1, file2)
    output = format_plain(diff)
    with open(file_path, 'r') as result:
        assert output == result.read()
        assert isinstance(output, str)


def test_plain_yaml():
    base_path = Path(__file__).parent
    file_path = (base_path / "../tests/fixtures/result_plain.txt").resolve()
    file1 = prepare_file('tests/fixtures/file1.yaml')
    file2 = prepare_file('tests/fixtures/file2.yaml')
    diff = generate_diff(file1, file2)
    output = format_plain(diff)
    with open(file_path, 'r') as result:
        assert output == result.read()
        assert isinstance(output, str)
