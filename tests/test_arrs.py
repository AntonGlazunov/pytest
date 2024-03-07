from utils import arrs
from utils import dicts

def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3]) == [1, 2, 3]
    assert arrs.my_slice([], 2) == []
    assert arrs.my_slice([1, 2, 3, 4], -3, -1) == [2, 3]

def test_get_val():
    assert dicts.get_val({"I": "Anton", "F": "Glazunov", "O": "Anatolevich"}, "F", "test") == "Glazunov"
    assert dicts.get_val({"I": "Anton", "F": "Glazunov", "O": "Anatolevich"}, "a") == "git"
    assert dicts.get_val({}, "a") == "git"
    assert dicts.get_val({}) == "git"