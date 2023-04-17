import pytest
from task_2 import create_yadisk_folder


@pytest.mark.parametrize(
    "folder, expected",
    [
        ("123", 201),
        ("123", 409),
        ("", 400),
        (".", 404),
    ],
)
def test_task_2(folder, expected):
    assert create_yadisk_folder(folder) == expected
