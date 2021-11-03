# from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    ans = 'Yes'
    N,W = map(int, input().split())
    memo = defaultdict(int)
    for _ in range(N):
        s,t,p = map(int, input().split())
        memo[s] += p
        memo[t] += -p
    A = [0]*(2*10**5+1)
    for key, value in memo.items():
        A[key] += value

    for i in range(len(A)):
        if i != 0:
            A[i] += A[i-1]
        if A[i] > W:
            ans = 'No'

    print(ans)

if __name__ == '__main__':
    main()