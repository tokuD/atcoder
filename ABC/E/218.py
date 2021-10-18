from typing import List,Union
import sys,heapq
input = sys.stdin.readline

class Node():

    def __init__(self, _id:int):
        self.id = _id
        self.marked = False
        self.edges:List[Edge] = []

class Edge():

    def __init__(self,_id:int, A:Node, B:Node, C:int):
        self.id = _id
        self.nodes:List[Node] = [A,B]
        self.C = C
        self.used = False

def main():
    N,M = map(int, input().split())
    nodes:List[Node] = [Node(i) for i in range(N)]
    edges:List[Edge] = [None]*M
    for i in range(M):
        A,B,C = map(int, input().split())
        A -= 1
        B -= 1
        edges[i] = Edge(i,nodes[A],nodes[B],C)
        nodes[A].edges.append(edges[i])
        nodes[B].edges.append(edges[i])

    #* プリム法でCの合計が最小になるように連結させる
    Q = []
    nodes[0].marked = True
    for edge in nodes[0].edges:
        heapq.heappush(Q, [edge.C, edge.id])
    #* Cが小さい順に取り出していく
    while len(Q) > 0:
        _,_id = heapq.heappop(Q)
        edge = edges[_id]
        new_node = None
        for node in edge.nodes:
            if node.marked:
                continue
            new_node = node

        if new_node is None:
            continue

        edge.used = True
        new_node.marked = True

        for next_edge in new_node.edges:
            if next_edge.used:
                continue
            heapq.heappush(Q, [next_edge.C, next_edge.id])

    ans = 0
    for edge in edges:
        if edge.used:
            continue
        if edge.C >= 0:
            ans += edge.C

    print(ans)

if __name__ == '__main__':
    main()