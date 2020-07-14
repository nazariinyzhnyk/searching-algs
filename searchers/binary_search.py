from registry import register_sorter


def recursive_bin_search(lst, el, r, l):
    if r >= l:
        mid = l + (r - l) // 2
        if lst[mid] == el:
            return mid
        elif lst[mid] > el:
            return recursive_bin_search(lst, el, mid - 1, l)
        else:
            return recursive_bin_search(lst, el, r, mid + 1)

    else:
        # Element is not present in the array
        return -1


def iterative_bin_search(lst, el):
    l = 0
    r = len(lst) - 1
    while r >= l:
        mid = l + (r - l) // 2
        if lst[mid] == el:
            return mid
        elif lst[mid] < el:
            l = mid + 1
        else:
            r = mid - 1
    return -1


@register_sorter
def binary_search(lst, el, rec=True):
    if rec:
        res = recursive_bin_search(lst, el, len(lst) - 1, 0)
    else:
        res = iterative_bin_search(lst, el)
    return res
