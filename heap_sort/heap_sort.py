def keyf_ascend(elem) -> int:
    return elem

def keyf_descend(elem) -> int:
    return -elem

def win2(array, i, j, key_function) -> int:
    assert i >= 0 and j >= 0
    assert i < len(array) and j < len(array)
    return i if key_function(array[i]) >= key_function(array[j]) else j

def is_leaf(N, i) -> bool:
    assert i >= 0 and i < N
    return i > N//2 - 1

def swap(array, i, j) -> None:
    assert i>=0 and j>=0
    assert i < len(array) and j < len(array)
    array[i], array[j] = array[j], array[i]

def has_only_one_child(N, i) -> bool:
    assert i>=0 and i<N
    return 2*i + 2 == N

def find_winner_n_swap(array, N, elem, key_function) -> int:
    if has_only_one_child(N, elem):
        winner = elem * 2 + 1
    else:
        winner = win2(array, elem*2 + 1, elem*2 + 2, key_function)
    abs_winner = win2(array, elem, winner, key_function)
    if abs_winner != elem:
        swap(array, abs_winner, elem)
    return abs_winner

def sift_down(array, N, elem, key_function) -> None:
    while not is_leaf(N, elem):
        winner = find_winner_n_swap(array, N, elem, key_function)
        if winner == elem:
            return
        elem = winner

def make_heap(array, key_function) -> None:
    N = len(array)
    for elem in range(N//2 - 1, -1, -1):
        sift_down(array, N, elem, key_function)

def heap_sort(array, key_function):
    make_heap(array, key_function)
    N = len(array)
    while N > 1:
        swap(array, 0, N - 1)
        N -= 1
        sift_down(array, N, 0, key_function)
