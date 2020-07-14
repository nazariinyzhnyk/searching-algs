search_algs = []


def register_sorter(sorter_func):
    """
    This function serve as a decorator to searching algs.
    All functions, decorated @register_sorter will be recorded in search_algs list.
    :param sorter_func: function to register
    """
    search_algs.append(sorter_func)
    return sorter_func
