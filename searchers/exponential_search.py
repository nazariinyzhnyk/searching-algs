from registry import register_sorter
from searchers.binary_search import recursive_bin_search


@register_sorter
def exponential_search(lst, el):
    if lst[0] == el:
        return 0

    i = 1
    while i < len(lst) and lst[i] <= el:
        i *= 2

    return recursive_bin_search(lst, el, min(i, len(lst)), int(i / 2))
