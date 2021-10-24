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
    H,W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = 'Yes'
    for i1 in range(H):
        for i2 in range(i1+1,H):
            for j1 in range(W):
                for j2 in range(j1,W):
                    if A[i1][j1] + A[i2][j2] <= A[i2][j1] + A[i1][j2]:
                        continue
                    else:
                        ans = 'No'
    print(ans)


if __name__ == '__main__':
    main()