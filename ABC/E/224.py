# from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
from collections import defaultdict
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
sys.setrecursionlimit(10**6)


class Node():

    def __init__(self, _id:int, r:int, c:int, a:int):
        self.id = _id
        self.r = r
        self.c = c
        self.a = a
        self.height = 0

H,W,N = map(int, input().split())
nodes: List[Node] = []
R = defaultdict(list)
C = defaultdict(list)
for i in range(N):
    r,c,a = map(int, input().split())
    nodes.append(Node(i,r,c,a))
    R[r].append(nodes[i])
    C[c].append(nodes[i])

def dfs(node:Node):
    if node.height > 0:
        return node.height

    r = node.r
    c = node.c
    a = node.a

    res = 0

    for child in R[r]:
        if child.a > a:
            if child.height > 0:
                res = max(res,child.height+1)
            else:
                res = max(res,dfs(child)+1)

    for child in C[c]:
        if child.a > a:
            if child.height > 0:
                res = max(res,child.height+1)
            else:
                res = max(res,dfs(child)+1)

    node.height = res
    return res

def main():
    ans = []
    for node in nodes:
        ans.append(dfs(node))

    for a in ans:
        print(a)

if __name__ == '__main__':
    main()