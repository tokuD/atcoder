from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
sys.setrecursionlimit(10**5)

class Node():

    def __init__(self, i:int, j:int):
        self.i = i
        self.j = j
        self.root:Node = self
        self.children:List[Node] = []
        self.parent:Node = None
        self.marked = False

def root(node:Node)->Node:
    pass

def main():
    H,W = map(int, input().split())
    nodes:List[List[Node]] = [[Node(i,j) for j in range(W)] for i in range(H)]
    Q = int(input())
    ans = []
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for _ in range(Q):
        q = list(map(lambda x:int(x)-1, input().split()))
        if q[0] == 0:
            r,c = q[1:]
            nodes[r][c].marked = True

            #* 4方向を見て赤マスがあれば自身を親に設定
            for i in range(4):
                node = nodes[r+dx[i]][c+dy[i]]
                count = 0
                if node.marked:
                    count += 1
                    #* 1個目は根を探索して自身をその根に付ける
                    root1 = None
                    if count == 1:
                        root1 = root(node)
                        nodes[r][c].root = root1
                    #* 2個目があった場合は2個目の根に1個目の根を設定する
                    if count > 1:
                        node.root = root1
        if q[0] == 1:
            ra,ca,rb,cb = q[1:]
            if nodes[ra][ca].root == nodes[rb][cb].root:
                ans.append('Yes')
            else:
                ans.append('No')


if __name__ == '__main__':
    main()