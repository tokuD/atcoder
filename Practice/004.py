#from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    N,M = map(int,input().split())
    A = [list(map(int,input().split())) for _ in range(N)]

    ans = 0

    for i,j in combinations(range(M),2):
        point = 0
        for n in range(N):
            point += max(A[n][i],A[n][j])
        ans = max(ans,point)

    print(ans)

if __name__ == '__main__':
    main()