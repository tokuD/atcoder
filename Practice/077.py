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
    mod = 10**5
    n,m = map(int, input().split())
    d = [int(input()) for _ in range(n-1)]
    a = [0] + [int(input()) for _ in range(m)]
    s = [0]*n
    for i in range(n-1):
        s[i+1] = s[i] + d[i]

    ans = 0
    start = 0
    for i in range(1,m+1):
        dl = a[i]
        ans += abs(s[start]-s[start+dl])
        ans %= mod
        start += dl

    print(ans)

if __name__ == '__main__':
    main()