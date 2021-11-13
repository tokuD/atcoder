# from __future__ import annotations
from typing import List,Union,Tuple,Dict,Set
import sys
input = sys.stdin.readline
from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    N = int(input())
    A = list(map(int, input().split()))
    count = [0]*3
    for a in A:
        count[a-1] += 1
    a,b,c = count
    dp = [[[0 for k in range(N+1)] for j in range(N+1)] for i in range(N+1)]

    if a-1>=0: dp[a-1][b][c] = 1
    if b-1>=0: dp[a][b-1][c] = 1
    if c-1>=0: dp[a][b][c-1] = 1

    for i in range(N)[::-1]:
        for j in range(N)[::-1]:
            for k in range(N)[::-1]:
                a = dp[i+1][j][k]
                b = dp[i][j+1][k]
                c = dp[i][j][k+1]
                if a!=0 and b!=0 and c!= 0:
                    dp[i][j][k] = ((a+1)*(i+1)+(b+1)*(j+1)+(c+1)*(k+1))/(i+j+k+3)
                elif a!= 0 and b!= 0 and c==0:
                    dp[i][j][k] = ((a+1)*(i+1)+(b+1)*(j+1))/(i+j+2)
                elif a!= 0 and b== 0 and c!=0:
                    dp[i][j][k] = ((a+1)*(i+1)+(c+1)*(k+1))/(i+k+2)
                elif a==0 and b!= 0 and c!=0:
                    dp[i][j][k] = ((b+1)*(j+1)+(c+1)*(k+1))/(j+k+2)
                elif a==0 and b==0 and c==0:
                    continue
                elif a != 0:
                    dp[i][j][k] = a+1
                elif b != 0:
                    dp[i][j][k] = b+1
                elif c != 0:
                    dp[i][j][k] = c+1

    print(dp[0][0][0])
    # print(dp)
    # print(dp[2][0][0])

if __name__ == '__main__':
    main()