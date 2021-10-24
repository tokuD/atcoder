from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
sys.setrecursionlimit(10**6)

class Node():

    def __init__(self, _id:int):
        self.id = _id
        self.child:List[Node] = []
        self.counter = 0
        self.visited = False

def dfs(node:Node):
    if node.visited:
        return
    node.visited = True

    for child in node.child:
        if child.visited:
            continue
        child.counter += node.counter
        dfs(child)

def main():
    N,Q = map(int, input().split())
    nodes = [Node(i) for i in range(N)]
    for _ in range(N-1):
        a,b = map(lambda x:int(x)-1, input().split())
        nodes[a].child.append(nodes[b])
        nodes[b].child.append(nodes[a])

    for _ in range(Q):
        p,x = map(int, input().split())
        p -= 1
        nodes[p].counter += x

    dfs(nodes[0])

    ans = []
    for node in nodes:
        ans.append(str(node.counter))

    print(' '.join(ans))




if __name__ == '__main__':
    main()