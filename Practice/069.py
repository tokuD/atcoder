# from __future__ import annotations
from typing import List,Union,Tuple,Dict,Set
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def Eratosthenes(N):
    """1~Nで素数を探す"""
    isprime = [True]*(N+1)
    isprime[0],isprime[1] = False,False
    for i in range(2,N+1):
        #* iが素数でない場合
        if not isprime[i]:
            continue
        #* iが素数なら、i以外のiの倍数をふるい落とす
        for j in range(2*i,N+1,i):
            isprime[j] = False
    #* isprime[i]:iが素数ならTrue
    return isprime

def main():
    Q = int(input())
    N = 10**5+1
    isprime = Eratosthenes(N)
    ok = [False]*(10**5+1)
    for i in range(2,10**5+1):
        if isprime[i] and isprime[(i+1)//2]:
            ok[i] = True

    cnt = [0]*(10**5+1) #* cnt[i]:iまでのokの数
    for i in range(1,10**5+1):
        cnt[i] = cnt[i-1]
        if ok[i]: cnt[i] += 1

    ans = []
    for _ in range(Q):
        l,r = map(int, input().split())
        ans.append(cnt[r]-cnt[l-1])

    for a in ans:
        print(a)


if __name__ == '__main__':
    main()