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
    A = []
    B = []
    total = 0
    for _ in range(N):
        a,b = map(int, input().split())
        A.append(a)
        B.append(b)
        total += a/b
    T = total / 2 #* 出会う時間
    t = 0
    i = 0
    dis = 0
    while True:
        a,b = A[i],B[i]
        if T < t + a/b:
            break
        t += a/b
        dis += a
        i += 1
    rest = T - t #* 残り時間
    dis += B[i] * rest
    print(dis)

if __name__ == '__main__':
    main()