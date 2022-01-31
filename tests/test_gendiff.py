from gendiff.gendiff import generate_diff
from pathlib import Path


def test_stylish_json():
    base_path = Path(__file__).parent
    file_path = (base_path / "../tests/fixtures/result_stylish.txt").resolve()
    path1 = 'tests/fixtures/file1.json'
    path2 = 'tests/fixtures/file2.json'
    output = generate_diff(path1, path2)
    with open(file_path, 'r') as result:
        assert output == result.read()
        assert isinstance(output, str)


def test_stylish_yaml():
    base_path = Path(__file__).parent
    file_path = (base_path / "../tests/fixtures/result_stylish.txt").resolve()
    path1 = 'tests/fixtures/file1.yaml'
    path2 = 'tests/fixtures/file2.yaml'
    output = generate_diff(path1, path2)
    with open(file_path, 'r') as result:
        assert output == result.read()
        assert isinstance(output, str)


def test_plain_json():
    base_path = Path(__file__).parent
    file_path = (base_path / "../tests/fixtures/result_plain.txt").resolve()
    path1 = 'tests/fixtures/file1.json'
    path2 = 'tests/fixtures/file2.json'
    output = generate_diff(path1, path2, 'plain')
    with open(file_path, 'r') as result:
        assert output == result.read()
        assert isinstance(output, str)


def test_plain_yaml():
    base_path = Path(__file__).parent
    file_path = (base_path / "../tests/fixtures/result_plain.txt").resolve()
    path1 = 'tests/fixtures/file1.yaml'
    path2 = 'tests/fixtures/file2.yaml'
    output = generate_diff(path1, path2, 'plain')
    with open(file_path, 'r') as result:
        assert output == result.read()
        assert isinstance(output, str)


def test_json():
    base_path = Path(__file__).parent
    file_path = (base_path / "../tests/fixtures/result_json.txt").resolve()
    path1 = 'tests/fixtures/file1.json'
    path2 = 'tests/fixtures/file2.json'
    output = generate_diff(path1, path2, 'json')
    with open(file_path, 'r') as result:
        assert output == result.read()
    path1 = 'tests/fixtures/file1.yaml'
    path2 = 'tests/fixtures/file2.yaml'
    output = generate_diff(path1, path2, 'json')
    with open(file_path, 'r') as result:
        assert output == result.read()
