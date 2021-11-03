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
    N,M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    ans = 'Yes'
    i0 = B[0][0] // 7 + 1
    j0 = B[0][0] % 7
    if j0 == 0:
        j0 = 7
        i0 -= 1

    for i in range(N):
        for j in range(M):
            b = B[i][j]
            if b == (i0-1+i)*7 + j0 + j:
                if not 1<= j0+j <= 7:
                    ans = 'No'
                continue
            else:
                ans = 'No'
    print(ans)

if __name__ == '__main__':
    main()