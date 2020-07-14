import time
import argparse

from registry import search_algs
import searchers

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--lst', nargs='+', type=int)
    parser.add_argument('--el', type=int)
    args = parser.parse_args()
    print(f'List to search in = {args.lst}. Elem to find = {args.el}')

    for sort_alg in search_algs:
        t1 = time.time()
        res = sort_alg(args.lst, args.el)
        print(f"\n{sort_alg.__name__}({args.lst}) = {res}. Time: {round(time.time() - t1, 2)}s.")


