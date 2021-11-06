# from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
import heapq
# sys.setrecursionlimit(10**5)

def main():
    INF = 10**20
    N,M,K,S = map(int, input().split())
    p,q = map(int, input().split())
    G = [[] for _ in range(N)] #* G[i]:街iから行ける街
    out = [False]*N #* ゾンビがいるかどうか
    fees = [p]*N #* 街iの宿泊費
    distance = [INF]*N
    for _ in range(K):
        c = int(input())
        c -= 1
        out[c] = True
        fees[c] = INF
    for _ in range(M):
        a,b = map(lambda x:int(x)-1, input().split())
        G[a].append(b)
        G[b].append(a)

    #* bfsで危険な町の宿泊費をqにする
    Q = deque()
    for i in range(N):
        if not out[i]: continue
        Q.append((0,i)) #* (通った道路の本数,今いる街)
    while len(Q)>0:
        dis,curr = Q.popleft()
        if distance[curr] != INF: continue
        if dis > S: continue
        distance[curr] = dis
        for nxt in G[curr]:
            if out[nxt]: continue
            Q.append((dis+1,nxt))

    for i in range(N):
        if 0 < distance[i] <= S:
            fees[i] = q

    fees[0] = 0
    fees[-1] = 0
    #* ダイクストラ法で最短経路を計算
    costs = [INF]*N #* 街iまでの宿泊費の最小値
    Q = [] #* (宿泊費の合計, 今いる街)
    heapq.heappush(Q,(0,0))
    while len(Q)>0:
        total,curr = heapq.heappop(Q)
        if costs[curr] != INF: continue
        costs[curr] = total
        for nxt in G[curr]:
            if out[nxt]: continue
            heapq.heappush(Q,(total+fees[nxt], nxt))

    print(costs[N-1])

if __name__ == '__main__':
    main()