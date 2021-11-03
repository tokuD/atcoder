# from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)

def main():
    N,Q = map(int, input().split())
    ans = []
    child = [-1] * (N+1) #* child[i]:電車iの後ろの電車
    par = [-1] * (N+1) #* par[i]:電車iの前の電車

    for _ in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            x,y = q[1:]
            child[x] = y
            par[y] = x
        elif q[0] == 2:
            x,y = q[1:]
            child[x] = -1
            par[y] = -1
        else:
            x = q[1]
            res = ''
            #* 親をたどっていく
            root = -1
            Q = deque()
            Q.append(x)
            while True:
                a = Q.popleft()
                if par[a] == -1:
                    root = a
                    break
                Q.append(par[a])
            #* 根から順に辿っていく
            Q = deque()
            Q.append(root)
            tmp = []
            count = 0
            while True:
                n = Q.popleft()
                tmp.append(str(n))
                count += 1
                if child[n] == -1: break
                Q.append(child[n])
            res = [str(count)] + tmp
            ans.append(res)

    for a in ans:
        print(' '.join(a))

if __name__ == '__main__':
    main()