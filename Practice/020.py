# from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    A.sort()
    C.sort()

    ans = 0

    for b in B:
        a = bisect_left(A, b)
        c = N - bisect_right(C, b)
        ans += a*c

    print(ans)


if __name__ == '__main__':
    main()