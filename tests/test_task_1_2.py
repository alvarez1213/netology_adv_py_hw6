import pytest

from task_1 import task_1_2


@pytest.mark.parametrize(
    "d, expected",
    [
        ({}, []),
        (
            {
                "user1": [1, 2, 1, 2, 1],
            },
            [1, 2],
        ),
        ({"user1": [1, 2, 1, 2, 1], "user2": [2, 2, 2]}, [1, 2]),
        (
            {
                "user1": [None],
                "user2": [1, 2, 1, 1, 1, 1],
                "user3": [],
            },
            [1, 2, None],
        ),
    ],
)
def test_task1_2(d, expected):
    assert task_1_2(d) == expected
