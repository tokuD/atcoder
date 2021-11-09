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
    N,K = map(int, input().split())
    A = list(map(int, input().split()))
    dic = defaultdict(int)
    for a in A:
        dic[a] += 1
    sorted_A = [] #* (楽しさの初期値,個数)
    for key,value in dic.items():
        sorted_A.append((key,value))
    sorted_A.sort(reverse=True)
    cnt = [None]*len(sorted_A)
    cnt[0] = sorted_A[0]
    for i in range(1,len(sorted_A)):
        cnt[i] = (sorted_A[i][0], cnt[i-1][1]+sorted_A[i][1])
    cnt.append((0,0))
    ans = 0
    for i in range(len(cnt)-1):
        now,dk = cnt[i]
        nxt = cnt[i+1][0]
        if K >= (now-nxt)*dk:
            K -= (now-nxt)*dk
            ans += (now-nxt)*(now+nxt+1)//2*dk
        else:
            a = K // dk #* 同じ楽しさで乗れる回数
            b = K % dk #* あまり
            ans += a*(now+now-a+1)//2*dk
            ans += (now-a)*b
            # print(a,b)
            break
        # print(ans)

    print(ans)
    # print(cnt)

if __name__ == '__main__':
    main()