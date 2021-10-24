# from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
sys.setrecursionlimit(10**7)

m = int(input())
n = int(input())
G = [list(map(int, input().split())) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(i:int, j:int, depth:int, visited:List[bool]):

    res = depth
    visited[i][j] = True

    for di,dj in zip(dy,dx):
        if not (0<=i+di<n and 0<=j+dj<m):
            continue
        if G[i+di][j+dj] == 0:
            continue
        if visited[i+di][j+dj]:
            continue
        res = max(res, dfs(i+di,j+dj,depth+1,visited))

    visited[i][j] = False

    return res

def main():

    ans = 0
    visited = [[False]*m for _ in range(n)]
    #* decide start
    for i in range(n):
        for j in range(m):
            if G[i][j] == 0:
                continue
            ans = max(ans, dfs(i,j,1,visited))

    print(ans)


if __name__ == '__main__':
    main()
