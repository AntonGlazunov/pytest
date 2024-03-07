import pytest

from utils import arrs
from utils import dicts


@pytest.fixture
def array_fixture():
    return [1, 2, 3, 4]


@pytest.fixture
def dict_fixture():
    return {"I": "Anton", "F": "Glazunov", "O": "Anatolevich"}


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice(array_fixture):
    assert arrs.my_slice(array_fixture, 1, 3) == [2, 3]
    assert arrs.my_slice(array_fixture, 1) == [2, 3, 4]
    assert arrs.my_slice(array_fixture) == [1, 2, 3, 4]
    assert arrs.my_slice([], 2) == []
    assert arrs.my_slice(array_fixture, -3, -1) == [2, 3]


def test_get_val(dict_fixture):
    assert dicts.get_val(dict_fixture, "F", "test") == "Glazunov"
    assert dicts.get_val(dict_fixture, "a") == "git"
    assert dicts.get_val({}, "a") == "git"
    assert dicts.get_val({}) == "git"
