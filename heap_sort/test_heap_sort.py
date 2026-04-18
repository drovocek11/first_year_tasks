import pytest
import random
from heap_sort import win2, is_leaf, swap, has_only_one_child, find_winner_n_swap, sift_down, make_heap, heap_sort
"""
TODO:
- в контракты функций swap, win2 добавить динамаическую длину N
- добавить компаратор в heap_sort
"""

@pytest.mark.parametrize("array, expected", [
    ([], []),
    ([1], [1]),
    ([1]*2, [1, 1]),
    ([1]*3, [1]*3),
    ([2]*4, [2]*4),
    (a:=[random.randint(-100, 100) for _ in range(100)], sorted(a)),
    (a:=[x for x in range(100)], sorted(a)),
    (a:=[x for x in range(100, -1, -1)], sorted(a)),
])
def test_heap_sort(array, expected):
    heap_sort(array)
    assert array == expected 


@pytest.mark.parametrize("array, expected", [
    ([1, 2, 3], [3, 2, 1]),
    ([2, 1], [2, 1]),
    ([1, 2], [2, 1]),
    ([1], [1]),
    ([], []),
    ([1, 2, 3, 4, 5, 6], [6, 5, 3, 4, 2, 1]),
    ([1, 2, 3, 4, 5], [5, 4, 3, 1, 2]),
])
def test_make_heap(array, expected):
    make_heap(array)
    assert array == expected


@pytest.mark.parametrize("array, elem, expected", [
    ([1, 2, 3], 0, [3, 2, 1]),
    ([1, 2], 0, [2, 1]),
    ([2, 1], 0, [2, 1]),
    ([1, 2, 3], 1, [1, 2, 3]),
    ([1], 0, [1]),
    ([2, 2, 1], 0, [2, 2, 1]),
    ([1, 2, 2], 0, [2, 1, 2]),
    ([2, 3, 1], 0, [3, 2, 1]),
    ([1, 2, 3, 4, 5, 6], 0, [3, 2, 6, 4, 5, 1]),
    ([1, 2, 2, 4, 5, 6], 0, [2, 5, 2, 4, 1, 6]),
    ([4, 5, 1, 2, 3, 6], 0, [5, 4, 1, 2, 3, 6]),
])
def test_sift_down(array, elem, expected):
    sift_down(array, len(array), elem)
    assert array == expected

@pytest.mark.parametrize("array, elem", [
    ([], 0),
    ([1], 1),
    ([1], -1)
])
def test_sift_down_exceptions(array, elem):
    with pytest.raises(AssertionError):
        sift_down(array, len(array), elem)


@pytest.mark.parametrize("array, elem, expected_array, expected_winner", [
    ([1, 2, 3], 0, [3, 2, 1], 2),
    ([1, 3, 2], 0, [3, 1, 2], 1),
    ([3, 2, 1], 0, [3, 2, 1], 0),
    ([1, 2], 0, [2, 1], 1),
    ([2, 1], 0, [2, 1], 0),
    ([1, 2, 3, 4, 5], 1, [1, 5, 3, 4, 2], 4),
    ([1, 2, 3, 5, 4], 1, [1, 5, 3, 2, 4], 3),
    ([1, 5, 3, 4, 2], 1, [1, 5, 3, 4, 2], 1),
    ([1, 2, 2], 0, [2, 1, 2], 1),
    ([2, 1, 1], 0, [2, 1, 1], 0),
    ([2, 2, 1], 0, [2, 2, 1], 0),
    ([2, 1, 2], 0, [2, 1, 2], 0),
    ([2, 2], 0, [2, 2], 0),
    ([1, 2, 3, 4, 5, 6], 2, [1, 2, 6, 4, 5, 3], 5),
    ([1, 2, 3, 2, 3], 1, [1, 3, 3, 2, 2], 4),
    ([1, 2, 6, 4, 5, 6], 2, [1, 2, 6, 4, 5, 6], 2),
])
def test_find_winner_n_swap(array, elem, expected_array, expected_winner): 
    winner = find_winner_n_swap(array, len(array), elem)
    assert winner == expected_winner
    assert array == expected_array 

@pytest.mark.parametrize("array, elem", [
    ([1, 2, 3], 1),
    ([1, 2, 3], 2),
    ([1, 2], 1),
    ([1, 2, 3, 4], 2),
    ([1, 2, 3, 4, 5], 2),
    ([1, 2, 3, 4, 5, 6], 3),
    ([1, 2, 3, 4, 5, 6], 4),
    ([1, 2, 3, 4, 5, 6], 5),
    ([], 0),
    ([1, 2, 3, 4, 5, 6], -1),
    ([1, 2, 3, 4, 5, 6], 6),
])
def test_find_winner_n_swap_exceptions(array, elem):
    with pytest.raises(AssertionError):
        find_winner_n_swap(array, len(array), elem)

@pytest.mark.parametrize("N, i", [
    (0, 0),
    (0, 1),
    (1, -1),
    (1, 1),
    (-1, 0),
    (-1, -1)
])
def test_has_only_one_child_exceptions(N, i):
    with pytest.raises(AssertionError):
        has_only_one_child(N, i)

@pytest.mark.parametrize("N, i, expected", [
    (1, 0, False),
    (2, 0, True),
    (3, 0, False),
    (4, 1, True),
    (5, 1, False),
    (6, 0, False),
    (6, 1, False),
    (6, 2, True),
    (6, 3, False),
    (6, 4, False),
    (6, 5, False)
])
def test_has_only_one_child(N, i, expected):
    assert has_only_one_child(N, i) == expected


@pytest.mark.parametrize("massive, i, j, expected", [
    ([1, 2, 3], 0, 1, [2, 1, 3]),
    ([1, 2, 3], 1, 2, [1, 3, 2]),
    ([1, 2, 3], 1, 0, [2, 1, 3]),
    ([1, 2, 3], 0, 0, [1, 2, 3]),
])
def test_swap(massive, i, j, expected):
    swap(massive, i, j)
    assert massive == expected


@pytest.mark.parametrize("massive, i, j", [
    ([], 0, 0),
    ([1, 2, 3], -1, 0),
    ([1, 2, 3], 0, -1),
    ([1, 2, 3], 3, 1),
    ([1, 2, 3], 0, 3),
])
def test_swap_exceptions(massive, i, j):
    with pytest.raises(AssertionError):
        swap(massive, i, j)


@pytest.mark.parametrize("N, i, expected", [
    (1, 0, True),
    (5, 2, True),
    (4, 0, False),
    (4, 1, False),
    (4, 2, True),
    (4, 3, True),
    (6, 0, False),
    (6, 1, False),
    (6, 2, False),
    (6, 3, True),
    (6, 4, True),
    (6, 5, True)
])
def test_is_leaf(N, i, expected):
    assert is_leaf(N, i) == expected


@pytest.mark.parametrize("N, i", [
    (0, 0),
    (1, 1),
    (1, -1),
    (2, 2),
    (2, -1),
    (-1, 0),
    (-1, -1)
])
def test_is_leaf_exceptions(N, i):
    with pytest.raises(AssertionError):
        is_leaf(N, i)


@pytest.mark.parametrize("array, i, j, expected", [
    ([1, 2, 3], 0, 1, 1),
    ([1], 0, 0, 0),
    ([1, 3, 2], 1, 2, 1),
    ([1, 1, 1], 0, 1, 0),
    ([-1, 2, 3], 0, 1, 1),
    ([1, 2, 3], 1, 0, 1),
    ([2, 2, 3], 1, 0, 1),
])
def test_win2(array, i, j, expected):
    assert win2(array, i, j) == expected

@pytest.mark.parametrize("array, i, j", [
    ([], 0, 0),
    ([1], 0, 1),
    ([1], 1, 0),
    ([1], -1, 0),
    ([1], 0, -1),
])
def test_win2_exceptions(array, i, j):
    with pytest.raises(AssertionError):
        win2(array, i, j)
