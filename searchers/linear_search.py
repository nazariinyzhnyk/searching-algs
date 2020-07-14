from registry import register_sorter


@register_sorter
def linear_search(lst, el):
    for i in range(len(lst)):
        if lst[i] == el:
            return i
    return -1
