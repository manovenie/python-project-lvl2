import pytest

from gendiff.file_parser import prepare_file


@pytest.mark.parametrize(
    'file_path',
    [
        ('tests/fixtures/wrong.ttt'),
        ('file_not_exists'),
    ],
)
def test_wrong_file(file_path):
    with pytest.raises(Exception):
        assert prepare_file(file_path)