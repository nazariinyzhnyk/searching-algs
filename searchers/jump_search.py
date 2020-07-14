import math
from registry import register_sorter


@register_sorter
def jump_search(lst, el):
    n = len(lst)
    step = round(math.sqrt(n))
    for i in range(0, len(lst), step):
        if lst[i] == el:
            return i
        elif lst[i] > el:
            for j in range(i - step, i):
                if lst[j] == el:
                    return j
    return -1
