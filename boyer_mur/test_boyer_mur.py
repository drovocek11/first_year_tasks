import pytest
from main import generate_char_table, max, index_after_shift, my_strstr, generate_char_table_new
from main import my_strstr_new

@pytest.mark.parametrize("second_number, expected", [
    (1, 1),
    (0, 1),
    (3, 3),
    (-1, 1),
])
def test_max(second_number, expected):
    assert max(1, second_number) == expected

@pytest.mark.parametrize("string, expected", [
    ("123", {"1":2, "2":1, "3":1}),
    ("abc", {"a":2, "b":1, "c":1}),
    ("1", {"1":1}),
    ("1488HH", {"1":5, "4":4, "8":2, "H":1}),
    ("", {}),
])
def test_generate_char_table(string, expected):
    assert generate_char_table(string) == expected

@pytest.mark.parametrize("string, expected", [
    ("a", {"a":1}),
    ("aa", {"a":1}),
    ("aaa", {"a":2}),
    ("ab", {"a":1, "b":1}),
    ("stringing", {"s":8, "t":7, "r":6, "i":5, "n":4, "g":3}),
])
def test_generate_char_table_new(string, expected):
    assert generate_char_table_new(string) == expected

@pytest.mark.parametrize("haystack, needle, last_index_needle, last_index_haystack, needle_shift_table, expected", [
    ("tree", "ee", 1, 1, generate_char_table("ee"), 3),
    ("tree", "tr", 1, 1, generate_char_table("tr"), 0),
    ("AbbA", "bb", 1, 1, generate_char_table("bb"), 2),
    ("AAAbbA", "bb", 1, 1, generate_char_table("bb"), 3),
    ("AAAbbA", "bb", 1, 3, generate_char_table("bb"), 4),
    ("AbbErtDF", "GreE", 3, 3, generate_char_table("GreE"), 6),
    ("AbbErtDF", "Gre", 2, 2, generate_char_table("Gre"), 5),
    ("xaca", "abca", 3, 3, generate_char_table("abca"), 4),
])
def test_index_after_shift(haystack, needle, last_index_needle, last_index_haystack, needle_shift_table, expected):
    j = last_index_needle
    i = last_index_haystack
    assert index_after_shift(haystack, needle, needle_shift_table, i, j) == expected

@pytest.mark.parametrize("func", [my_strstr, my_strstr_new])
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
    ("xaca", "abca", -1),
    ("xaca......", "abca", -1),
    ("aaabcaxaca......", "abca", 2),
    ("11231xaca......", "abca", -1),
])
def test_my_strstr(func, haystack, needle, expected):
    assert func(haystack, needle) == expected
