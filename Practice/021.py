# from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def judge(x:int, N:int, H:List[int], S:List[int])->bool:
    """xを越えずに割ることができるか"""
    #* add[i]:i秒以内に割れば大丈夫な風船の数
    tmp = [0]*N
    for h,s in zip(H,S):
        t = min(N-1, (x-h) // s)
        if t < 0:
            return False
        tmp[t] += 1
    add = [0]*N
    add[0] = tmp[0]

    for i in range(N-1):
        add[i] = add[i-1] + tmp[i]
        if add[i] > i+1:
            return False

    return True


def main():
    N = int(input())
    H = []
    S = []
    for _ in range(N):
        h,s = map(int, input().split())
        H.append(h)
        S.append(s)

    ok = max(H) + max(S) * (N-1)
    ng = 1
    while ok - ng > 1:
        x = (ok+ng) // 2
        if judge(x, N, H, S):
            ok = x
        else:
            ng = x

    print(ok)


if __name__ == '__main__':
    main()