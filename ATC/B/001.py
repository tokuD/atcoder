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
        self.root = self #* 根のインスタンス
        self.parent:Node = None #* 親のインスタンス

def root(n:Node)->Node:
    """頂点nの根のインスタンスを返す(道中で通った頂点は直接根につなぐ)"""

    #* 親がいない時
    if n.parent is None:
        return n.root

    #* 親がいる場合、親を順にたどっていく
    n.root = root(n.parent)

    #* 根を直接の親とする
    n.parent = n.root

    return n.root

def main():
    N,Q = map(int, input().split())
    nodes = [Node(i) for i in range(N)]
    ans = []
    for _ in range(Q):
        p,a,b = map(int, input().split())
        if p == 0:
            #* bの根をaの根に付ける
            roota = root(nodes[a])
            rootb = root(nodes[b])
            if roota == rootb:
                continue
            rootb.parent = roota
            rootb.root = roota
        else:
            #* a,bのrootが同じかを判定しながら、探索した頂点は根に直接つなげる
            roota = root(nodes[a])
            rootb = root(nodes[b])
            if roota == rootb:
                ans.append('Yes')
            else:
                ans.append('No')
            pass

    # for node in nodes:
    #     if node.parent is None:
    #         print(node.parent)
    #     else:
    #         print(node.parent.id)

    for a in ans:
        print(a)


if __name__ == '__main__':
    main()