from registry import register_sorter


@register_sorter
def interpolation_search(lst, el):
    lo = 0
    hi = len(lst) - 1
    while hi >= lo and lst[lo] <= el <= lst[hi]:
        pos = int(lo + (el-lst[lo]) * (hi-lo) / (lst[hi]-lst[lo]))
        if lst[pos] == el:
            return pos
        elif lst[pos] < el:
            lo = pos + 1
        else:
            hi = pos - 1
    return -1
