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
    N = int(input())
    A = list(map(int, input().split()))
    S = [0]*(N+1)
    for i in range(N):
        S[i+1] = S[i] + A[i]

    ans = []
    for k in range(1,N+1):
        res = 0
        for g in range(k,N+1):
            res = max(res, S[g]-S[g-k])
        ans.append(res)

    for a in ans:
        print(a)

if __name__ == '__main__':
    main()