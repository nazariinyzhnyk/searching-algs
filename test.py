from registry import search_algs
import searchers

print('\nCurrently available sorting algs:', [search_alg.__name__ for search_alg in search_algs])


def dummy_test():
    lst = [1, 2, 3, 4, 5, 9, 34, 56, 87, 92]
    val = 56
    print('\nEntered dummy test to sort list: ', lst)

    for sort_alg in search_algs:
        res = sort_alg(lst, val)
        print(f"\n{sort_alg.__name__}({lst}) = {res}")
        print(f"Actual index: {lst.index(val)}\nFound index : {res}")


if __name__ == '__main__':
    dummy_test()
