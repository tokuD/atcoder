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
    n = int(input())
    S = list(map(int, input().split()))
    q = int(input())
    T = list(map(int, input().split()))
    ans = 0

    for t in T:
        a = bisect_left(S, t)
        if a >= n:
            continue
        if S[a] == t:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()