# from __future__ import annotations
from typing import List,Union,Tuple,Dict,Set
import sys
input = sys.stdin.readline
from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    H,W = map(int, input().split())
    C = []
    for _ in range(10):
        c = list(map(int, input().split()))
        C.append(c)
    num = defaultdict(int)
    for _ in range(H):
        A = list(map(int, input().split()))
        for a in A:
            if a == -1: continue
            num[a] += 1

    for k in range(10):
        for x in range(10):
            for y in range(10):
                C[x][y] = min(C[x][y], C[x][k]+C[k][y])

    ans = 0
    for key,value in num.items():
        ans += value*C[key][1]

    print(ans)

if __name__ == '__main__':
    main()