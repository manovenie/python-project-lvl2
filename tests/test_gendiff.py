import pytest
from gendiff.gendiff import generate_diff
from pathlib import Path


def test_plain_json():
    base_path = Path(__file__).parent
    file_path = (base_path / "../tests/fixtures/result_plain.txt").resolve()
    with open(file_path, 'r') as result:
        assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == result.read()
        assert type(generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')) == str


def test_plain_yaml():
    base_path = Path(__file__).parent
    file_path = (base_path / "../tests/fixtures/result_plain.txt").resolve()
    with open(file_path, 'r') as result:
        assert generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml') == result.read()
        assert type(generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml')) == str