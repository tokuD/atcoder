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

    def __init__(self, _id:int):
        self.id:int = _id
        self.color:bool = True
        self.child:List[Node] = []
        self.visited:bool = False

def dfs(curr:Node, group1:List[str], group2:List[str]):
    if curr.visited:
        return
    curr.visited = True

    if curr.color:
        group1.append(str(curr.id + 1))
    else:
        group2.append(str(curr.id + 1))

    for child in curr.child:
        child.color = not curr.color
        dfs(child,group1,group2)


def main():
    N = int(input())
    nodes = [Node(i) for i in range(N)]
    for _ in range(N-1):
        a,b = map(lambda x:int(x)-1, input().split())
        nodes[a].child.append(nodes[b])
        nodes[b].child.append(nodes[a])

    #* 頂点0からdfsで交互に色分け
    group1 = []
    group2 = []
    dfs(nodes[0],group1,group2)

    #* 長さがN/2以上ある方からN/2個の頂点を取り出す
    if len(group1) >= N//2:
        print(' '.join(group1[:N//2]))
    else:
        print(' '.join(group2[:N//2]))



if __name__ == '__main__':
    main()