# from __future__ import annotations
from typing import List,Union,Tuple,Dict,Set
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    H,W = map(int, input().split())
    G = []
    for _ in range(H):
        a = list(input().rstrip())
        G.append(a)

    row = []
    column = []
    for i in range(H):
        flag = True
        for j in range(W):
            if G[i][j] == '#':
                flag = False
        if flag:
            row.append(i)

    for j in range(W):
        flag = True
        for i in range(H):
            if G[i][j] == '#':
                flag = False
        if flag:
            column.append(j)

    ans = []
    for i in range(H):
        res = []
        if i in row: continue
        for j in range(W):
            if j in column: continue
            res.append(G[i][j])
        ans.append(res)

    for a in ans:
        print(''.join(a))

if __name__ == '__main__':
    main()