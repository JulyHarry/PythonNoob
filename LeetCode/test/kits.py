import os
from itertools import zip_longest

from LeetCode.test.wrapper import timeit_log, timeit_print


@timeit_print
def compare_files(a, b):
    if not os.path.exists(a):
        print(f"file [{a}] not exists")
    if not os.path.exists(b):
        print(f"file [{b}] not exists")
    i = 0
    j = 0
    with open(a, 'r') as f1, open(b, 'r') as f2:
        for line1, line2 in zip_longest(f1.readlines(), f2.readlines()):
            i += 1
            if line1: line1 = line1.strip()
            if line2: line2 = line2.strip()
            if line1 != line2:
                j += 1
                print(f"[{i}] {line1} {line2}")
        print(f'一共 {j} 个不同的地方')


if __name__ == '__main__':
    compare_files('/Users/hang/Downloads/P3379_1.out', 'test.out')
