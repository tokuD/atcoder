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
    V,E = map(int, input().split())
    dis = [[INF]*V for _ in range(V)]
    for _ in range(E):
        s,t,d = map(int, input().split())
        dis[s][t] = d
    for i in range(V):
        dis[i][i] = 0

    # for _ in range(2):
    for k in range(V):
        for x in range(V):
            for y in range(V):
                if dis[x][k] == INF or dis[k][y] == INF: continue
                dis[x][y] = min(dis[x][y],dis[x][k]+dis[k][y])

    flag = False
    ans = [['INF']*V for _ in range(V)]
    for i in range(V):
        if dis[i][i] < 0: flag = True
        for j in range(V):
            if dis[i][j] == INF: continue
            ans[i][j] = str(dis[i][j])

    if flag:
        print('NEGATIVE CYCLE')
    else:
        for a in ans:
            print(' '.join(a))

    # print(dis)

if __name__ == '__main__':
    main()