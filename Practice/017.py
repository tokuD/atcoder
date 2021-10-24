# from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
from collections import defaultdict,deque
from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def check(seq:tuple):
    dic1 = defaultdict(int)
    dic2 = defaultdict(int)
    for x,y in enumerate(seq):
        dic1[x-y] += 1
        dic2[x+y] += 1

    res = True

    for v in dic1.values():
        if v >= 2:
            res = False

    for v in dic2.values():
        if v >= 2:
            res = False

    return res

def main():
    k = int(input())
    Q = [-1 for _ in range(8)]
    for _ in range(k):
        r,c = map(int, input().split())
        Q[r] = c

    ans = [['.']*8 for _ in range(8)]

    for seq in permutations(range(8)):
        flag = True
        if not check(seq):
            continue
        for i,x in enumerate(seq):
            if Q[i] != -1 and x != Q[i]:
                flag = False
                break
        if not flag:
            continue
        for i,x in enumerate(seq):
            ans[i][x] = 'Q'

    for a in ans:
        print(''.join(a))

if __name__ == '__main__':
    main()