#from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    N,M = map(int,input().split())
    connected: List[int] = [] #* connected[i]: i番目の電球のスイッチの接続状況(bit列で表現)

    for i in range(M):
        q = list(map(int,input().split()))
        k = q[0]
        bit = 0
        for s in q[1:]:
            bit += 2**(s-1)
        connected.append(bit)

    even = list(map(int,input().split())) #* odd_even[i]: i番目の電球が偶数個のスイッチでつくかどうか

    ans = 0

    #* スイッチのon,offを表すbitループ
    for i in range(2**N):
        ok = 0 #* 点灯した電球の数
        for j in range(M): #* 電球のループ
            lighted = 0 #* onのスイッチの数
            for k in range(N):
                if ((i&connected[j]) >> k) & 1:
                    lighted += 1
            if lighted % 2 == even[j]:
                ok += 1
        if ok == M:
            ans += 1

    print(ans)





if __name__ == '__main__':
    main()