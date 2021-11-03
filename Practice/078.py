# from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def convert(x):
    if x == 'J': return 0
    if x == 'O': return 1
    if x == 'I': return 2

def main():
    M,N = map(int, input().split())
    K = int(input())
    G = [list(map(convert,input().rstrip())) for _ in range(M)]
    Q = [list(map(lambda x:int(x)-1, input().split())) for _ in range(K)]
    S = [[[0,0,0] for i in range(N)]  for _ in range(M)] #* S[i][j]:(i,j)までの(J,O,I)の和
    for i in range(M):
        for j in range(N):
            S[i][j][G[i][j]] += 1
            if i != 0 and j != 0:
                for k in range(3):
                    S[i][j][k] += S[i-1][j][k]
                    S[i][j][k] += S[i][j-1][k]
                    S[i][j][k] -= S[i-1][j-1][k]
            if i == 0 and j != 0:
                for k in range(3):
                    S[i][j][k] += S[i][j-1][k]
            if i != 0 and j == 0:
                for k in range(3):
                    S[i][j][k] += S[i-1][j][k]

    ans = []
    for q in Q:
        a,b,c,d = q
        res = []
        for k in range(3):
            tmp = 0
            tmp += S[c][d][k]
            if b>0:
                tmp -= S[c][b-1][k]
            if a>0:
                tmp -= S[a-1][d][k]
            if a>0 and b>0:
                tmp += S[a-1][b-1][k]
            res.append(str(tmp))
        ans.append(res)

    for a in ans:
        print(' '.join(a))

if __name__ == '__main__':
    main()