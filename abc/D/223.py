#from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
import heapq
# sys.setrecursionlimit(10**5)

class Node():

    def __init__(self, num:int):
        self.num = num
        self.parents:dict[int] = {} #* 親のnum
        self.child:dict[int] = {} #* 子のnum

def main():
    N,M = map(int, input().split())
    nodes = [Node(i) for i in range(N+1)]
    for _ in range(M):
        a,b = map(int, input().split())
        #* bの親にaを追加
        nodes[b].parents[a] = 1
        nodes[a].child[b] = 1

    ans = []
    Q = []
    for node in nodes[1:]:
        if len(node.parents) == 0:
            heapq.heappush(Q, node.num)

    while len(Q) > 0:
        ind = heapq.heappop(Q)
        node = nodes[ind]
        ans.append(str(node.num))

        #* 子供のparentsから自身を削除し、親がいなくなればheapに追加
        for chi in node.child:
            child = nodes[chi]
            child.parents.pop(ind)
            if len(child.parents) == 0:
                heapq.heappush(Q, child.num)

    if len(ans) == N:
        print(' '.join(ans))
    else:
        print(-1)

if __name__ == '__main__':
    main()