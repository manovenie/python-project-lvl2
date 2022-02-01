import pytest
from gendiff.gendiff import generate_diff
from pathlib import Path


@pytest.mark.parametrize(
    'style, file_before, file_after, file_result',
    [
        ('plain', 'tests/fixtures/file1.json', 'tests/fixtures/file2.json', '../tests/fixtures/result_plain.txt'),  # noqa:E501
        ('plain', 'tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml', '../tests/fixtures/result_plain.txt'),  # noqa:E501
        ('stylish', 'tests/fixtures/file1.json', 'tests/fixtures/file2.json', '../tests/fixtures/result_stylish.txt'),  # noqa:E501
        ('stylish', 'tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml', '../tests/fixtures/result_stylish.txt'),  # noqa:E501
        ('json', 'tests/fixtures/file1.json', 'tests/fixtures/file2.json', '../tests/fixtures/result_json.txt'),  # noqa:E501
        ('json', 'tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml', '../tests/fixtures/result_json.txt'),  # noqa:E501
    ],
)
def test_generate_diff(style, file_before, file_after, file_result):
    base_path = Path(__file__).parent
    file_result_path = (base_path / file_result).resolve()
    with open(file_result_path, 'r') as file:
        result = file.read()
    assert generate_diff(file_before, file_after, style) == result
