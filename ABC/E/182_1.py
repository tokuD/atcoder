# from __future__ import annotations
from typing import List,Union,Tuple,Dict,Set
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
sys.setrecursionlimit(10**5)

class Node():

    def __init__(self, H:int, W:int):
        self.G:List[List[int]] = [[0]*(W+2) for _ in range(H+2)] #* 1:電球, 2:ブロック
        self.lighted:List[List[bool]] = [[False]*(W+2) for _ in range(H+2)]
        self.count = 0
        for i in range(H+2):
            self.G[i][0] = 2
            self.G[i][-1] = 2
        for j in range(W+2):
            self.G[0][j] = 2
            self.G[-1][j] = 2

    def dfs(self,i:int,j:int,di:int,dj:int):
        """
        各マスからブロックか電球につくまで4方向にdfsする
        電球についた場合は、道中のマスも全て点灯させる
        """
        if self.G[i][j] == 1:
            # self.count += 1
            self.lighted[i][j] = True
            return True
        if self.G[i][j] == 2:
            return False
        if self.dfs(i+di,j+dj,di,dj):
            # self.count += 1
            self.lighted[i][j] = True
            return True

def main():
    dxdy = [(1,0),(-1,0),(0,1),(0,-1)]
    H,W,N,M = map(int, input().split())
    nodes = Node(H,W)
    for _ in range(N):
        a,b = map(int, input().split())
        nodes.G[a][b] = 1
    for _ in range(M):
        c,d = map(int, input().split())
        nodes.G[c][d] = 2

    for i in range(1,H+1):
        for j in range(1,W+1):
            #* 点灯済みのマスは飛ばす
            if nodes.lighted[i][j]: continue
            for di,dj in dxdy:
                nodes.dfs(i,j,di,dj)

    ans = 0
    for i in range(1,H+1):
        for j in range(1,W+1):
            if nodes.lighted[i][j]:
                ans += 1

    print(ans)

if __name__ == '__main__':
    main()