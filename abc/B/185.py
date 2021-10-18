# from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    N,M,T = map(int, input().split())
    last = 0
    now = N
    ans = 'Yes'
    for _ in range(M):
        a,b = map(int, input().split())
        now -= (a-last)
        if now <= 0:
            ans = 'No'
        now += b-a
        now = min(now,N)
        last = b

    now -= T-last
    if now <= 0:
        ans = 'No'

    print(ans)


if __name__ == '__main__':
    main()