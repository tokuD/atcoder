# from __future__ import annotations
from typing import List,Union,Tuple,Dict,Set
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    INF = 10**20
    N = int(input())
    X = []
    Y = []
    Z = []
    for _ in range(N):
        x,y,z = map(int, input().split())
        X.append(x)
        Y.append(y)
        Z.append(z)

    #* 先に、ワーシャルフロイド法で各都市間の最小コストを計算しておく
    dis = [[INF]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                dis[i][j] = 0
                continue
            dis[i][j] = abs(X[j]-X[i]) + abs(Y[j]-Y[i]) + max(0,Z[j]-Z[i])

    for k in range(N):
        for x in range(N):
            for y in range(N):
                dis[x][y] = min(dis[x][y], dis[x][k]+dis[k][y])

    #* dp[i][j]:今までに通った都市のbit列がiの時の最小コスト,jは最後に通った都市
    dp = [[INF]*N for _ in range(2**N)]

    for i in range(1,N):
        dp[1<<i][i] = dis[0][i]

    for i in range(2**N):
        for j in range(N):
            if dp[i][j] == INF: continue
            if (i>>j)&1==0: continue

            #* j->kへの移動
            for k in range(N):
                if (i>>k)&1==1: continue
                dp[i|(1<<k)][k] = min(dp[i|(1<<k)][k],dp[i][j]+dis[j][k])

    ans = dp[-1][0]
    print(ans)

if __name__ == '__main__':
    main()