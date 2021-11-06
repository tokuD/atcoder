# from __future__ import annotations
from typing import List,Union,Tuple,Dict,Set
import sys
input = sys.stdin.readline
from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
import heapq
# sys.setrecursionlimit(10**5)

def bfs(N:int,R:List[int], G:List[List[int]],G0:List[List[int]]):
    for s in range(N):
        Q = deque() #* (通った道路の本数,今いる町)
        Q.append((0,s))
        visited = [False]*N
        while len(Q)>0:
            dis,curr = Q.popleft()
            if dis > R[s]: break
            if visited[curr]: continue
            visited[curr] = True
            if curr != s: G0[s].append(curr)
            for nxt in G[curr]:
                if visited[nxt]: continue
                if dis+1>R[s]: continue
                Q.append((dis+1, nxt))
    return


def main():
    N,K = map(int, input().split())
    C = []
    R = []
    for _ in range(N):
        c,r = map(int, input().split())
        C.append(c)
        R.append(r)
    G = [[] for _ in range(N)]
    for _ in range(K):
        a,b = map(lambda x:int(x)-1, input().split())
        G[a].append(b)
        G[b].append(a)

    #* bfsで各町から乗り継ぎなしで行ける町を求めておく
    G0 = [[] for _ in range(N)]
    bfs(N,R,G,G0)

    fees = [-1]*N
    Q = [] #* (自身込みの運賃,今いる町)
    heapq.heappush(Q,(C[0],0))
    while len(Q)>0:
        fee,curr = heapq.heappop(Q)
        if fees[-1] != -1: break
        if fees[curr] != -1: continue
        fees[curr] = fee - C[curr]
        for nxt in G0[curr]:
            if fees[nxt] != -1: continue
            heapq.heappush(Q,(fee+C[nxt], nxt))

    print(fees[N-1])

if __name__ == '__main__':
    main()