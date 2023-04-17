import pytest

from task_1 import task_1_1


@pytest.mark.parametrize(
    "list_of_dicts, expected",
    [
        (
            [
                {"visit1": ["Москва", "Россия"]},
                {"visit2": ["Дели", "Индия"]},
            ],
            [{"visit1": ["Москва", "Россия"]}],
        ),
        ([], []),
        (
            [
                {"visit2": ["Дели", "Индия"]},
            ],
            [],
        ),
    ],
)
def test_task1_1(list_of_dicts, expected):
    assert task_1_1(list_of_dicts) == expected
