def max(b, a=1):
    return a if a > b else b

def generate_table(needle: str) -> dict:
    table = {}
    index = 0
    for i in needle:
        table[i] = max(len(needle) - index - 1)
        index += 1
    return table

def key_is_exist(table: dict, key: str) -> bool:
    for i in table:
        if i == key:
            return True
    return False

def is_same_elems(haystack_elem: str, needle_elem: str) -> bool:
    return haystack_elem == needle_elem

def index_after_shift(haystack, needle, needle_shift_table, i, j) -> int:
    for haystack_elem, needle_elem in zip(range(i, -1, -1), range(j, -1, -1), strict=False):
        if is_same_elems(haystack[haystack_elem], needle[needle_elem]):
            continue
        if key_is_exist(needle_shift_table, key := haystack[haystack_elem]):
            return haystack_elem + needle_shift_table[key]
        return haystack_elem + len(needle)
    return 0

def my_strstr(haystack: str, needle: str) -> int:
    if needle == "" or len(needle) > len(haystack):
        return -1
    j = len(needle) - 1
    i = j
    while i < len(haystack):
        saved_i = i
        i = index_after_shift(haystack, needle, generate_table(needle), i, j)
        if i == 0:
            return saved_i - len(needle) + 1
    else:
        return -1


    
