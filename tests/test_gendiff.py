import pytest
from gendiff.gendiff import generate_diff
from pathlib import Path
from gendiff.parser import prepare_file


def test_plain_json():
    base_path = Path(__file__).parent
    file_path = (base_path / "../tests/fixtures/result_plain.txt").resolve()
    file1 = prepare_file('tests/fixtures/file1.json')
    file2 = prepare_file('tests/fixtures/file2.json')
    with open(file_path, 'r') as result:
        assert generate_diff(file1, file2) == result.read()
        assert type(generate_diff(file1, file2)) == str


def test_plain_yaml():
    base_path = Path(__file__).parent
    file_path = (base_path / "../tests/fixtures/result_plain.txt").resolve()
    file1 = prepare_file('tests/fixtures/file1.yaml')
    file2 = prepare_file('tests/fixtures/file2.yaml')
    with open(file_path, 'r') as result:
        assert generate_diff(file1, file2) == result.read()
        assert type(generate_diff(file1, file2)) == str