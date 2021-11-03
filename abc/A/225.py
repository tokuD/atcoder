# from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def calc(N):
    res = 1
    for n in range(1,N+1):
        res *= n
    return res

def main():
    S = list(input().rstrip())
    N = len(S)
    abc = defaultdict(int)
    for s in S:
        abc[s] += 1

    ans = calc(N)

    for key,value in abc.items():
        a = calc(value)
        ans //= a
    print(ans)


if __name__ == '__main__':
    main()