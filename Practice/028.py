# from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
from collections import deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

class Node():

    def __init__(self, _id:int):
        self.id = _id
        self.child: List[Node] = []
        self.distance: int = -1
        self.visited: bool = False

def main():
    n = int(input())
    nodes = [Node(i) for i in range(n)]
    for _ in range(n):
        q = list(map(lambda x:int(x)-1, input().split()))
        u = q[0]
        for i in range(q[1]+1):
            v = q[i+2]
            nodes[u].child.append(nodes[v])

    Q: deque[Union[Node, int]] = deque()
    Q.append((nodes[0],0))

    while len(Q) > 0:
        node, d= Q.popleft()
        if node.visited:
            continue
        node.visited = True
        node.distance = d

        for child in node.child:
            Q.append((child, d+1))

    for node in nodes:
        print(node.id+1, node.distance)

if __name__ == '__main__':
    main()