def max(a, b):
    return a if a > b else b


def generate_char_table_new(needle:str) -> dict:
    table = dict()
    index = 0
    for char in needle:
        if char in table.keys():
            index += 1
            continue
        table[char] = max(1, len(needle) - index - 1)
        index += 1
    return table

def generate_char_table(needle: str) -> dict:
    table = dict()
    index = 0
    for char in needle:
        table[char] = max(1, len(needle) - index - 1)
        index += 1
    return table

def index_after_shift(haystack, needle, needle_shift_table, i, j) -> int:
    for haystack_elem, needle_elem in zip(range(i, -1, -1), range(j, -1, -1), strict=False):
        if haystack[haystack_elem] == needle[needle_elem]:
            continue
        key = haystack[haystack_elem]
        if key in needle_shift_table.keys():
            new_index = haystack_elem + needle_shift_table[key]
            return new_index if new_index > i else i + 1            
        return haystack_elem + len(needle)
    return 0

def my_strstr(haystack: str, needle: str) -> int:
    if needle == "" or len(needle) > len(haystack):
        return -1
    j = len(needle) - 1
    i = j
    char_table = generate_char_table(needle)
    while i < len(haystack):
        saved_i = i
        i = index_after_shift(haystack, needle, char_table, i, j)
        if i == 0:
            return saved_i - len(needle) + 1 
    return -1

def my_strstr_new(haystack: str, needle: str) -> int:
    if needle == "" or len(needle) > len(haystack):
        return -1
    j = len(needle) - 1
    i = j
    char_table = generate_char_table_new(needle)
    while i < len(haystack):
        saved_i = i
        i = index_after_shift(haystack, needle, char_table, i, j)
        if i == 0:
            return saved_i - len(needle) + 1 
    return -1

