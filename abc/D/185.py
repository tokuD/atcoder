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
    A = [0] + list(map(int, input().split())) + [N+1]
    A.sort()
    if len(A) == 2:
        print(1)
        exit()

    INF = 10**10
    k = INF
    dis = []
    for i in range(M+1):
        d = A[i+1] - A[i] - 1
        if d == 0:
            continue
        k = min(k,d)
        dis.append(d)
    if k == INF:
        print(0)
        exit()

    ans = 0
    for d in dis:
        if d % k == 0:
            ans += d // k
        else:
            ans += d//k + 1
    print(ans)

if __name__ == '__main__':
    main()