import pytest
from main import generate_table, max, key_is_exist, is_same_elems, index_after_shift, my_strstr

@pytest.mark.parametrize("second_number, expected", [
    (1, 1),
    (0, 1),
    (3, 3),
    (-1, 1),
])
def test_max(second_number, expected):
    assert max(second_number) == expected

@pytest.mark.parametrize("string, expected", [
    ("123", {"1":2, "2":1, "3":1}),
    ("abc", {"a":2, "b":1, "c":1}),
    ("1", {"1":1}),
    ("1488HH", {"1":5, "4":4, "8":2, "H":1}),
    ("", {}),
])
def test_generate_table(string, expected):
    assert generate_table(string) == expected

@pytest.mark.parametrize("dict, key, expected", [
    ({"1":5, "4":4, "8":2, "H":1}, "H", True),
    ({"1":5, "4":4, "8":2, "H":1}, "2", False),
    ({}, "H", False),
    ({"H":3}, "H", True),
    ({"H":3}, "T", False)
])
def test_key_check(dict, key, expected):
    assert key_is_exist(dict, key) == expected

@pytest.mark.parametrize("haystack_elem, needle_elem, expected", [
    ("", "", True),
    ("1", "1", True),
    ("1", "0", False),
    ("0", "1", False),
    ("A", "a", False)
])
def test_is_same(haystack_elem, needle_elem, expected):
    assert is_same_elems(haystack_elem, needle_elem) == expected

@pytest.mark.parametrize("haystack, needle, last_index_needle, needle_shift_table, expected", [
    ("tree", "ee", 1, generate_table("ee"), 3),
    ("tree", "tr", 1, generate_table("tr"), 0),
    ("AbbA", "bb", 1, generate_table("bb"), 2),
    ("AbbErtDF", "GreE", 2, generate_table("GreE"), 6),
])
def test_index_after_shift(haystack, needle, last_index_needle, needle_shift_table, expected):
    j = last_index_needle
    i = j
    assert index_after_shift(haystack, needle, needle_shift_table, i, j) == expected

@pytest.mark.parametrize("haystack, needle, expected", [
    ("babokat123", "", -1),
    ("babokat123", "kat", 4),
    ("ka", "kat", -1),
    ("babokat123", "123", 7),
    ("babokat123", "bab", 0),
    ("babokat123", "a", 1),
    ("babokat123", "bo", 2),
    ("babo123kat123", "123", 4),
    ("babokat123", "RE", -1),
    ("babokat123", "babokat123", 0),
])
def test_my_strstr(haystack, needle, expected):
    assert my_strstr(haystack, needle) == expected
