#from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
sys.setrecursionlimit(10**5)

def dfs(ind:int, tmp:int, A:List, ok:set):
    if ind == len(A):
        return
    a = A[ind]

    #* aを使う場合
    ok.add(tmp+a)
    dfs(ind+1, tmp+a,A, ok)

    #* aを使わない場合
    ok.add(tmp)
    dfs(ind+1, tmp, A, ok)


def main():
    n = int(input())
    A = list(map(int,input().split()))
    q = int(input())
    M = list(map(int,input().split()))

    ok = set()

    dfs(0, 0, A, ok)

    ans = []

    for m in M:
        if m in ok:
            ans.append('yes')
        else:
            ans.append('no')

    for a in ans:
        print(a)


if __name__ == '__main__':
    main()