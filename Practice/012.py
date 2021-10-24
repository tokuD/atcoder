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
    knowned = set()
    for _ in range(M):
        x,y = map(lambda x:int(x)-1,input().split())
        knowned.add((x,y))

    ans = 0
    
    for bit in range(2**N):
        flag = True
        count = 0
        for i in range(N):
            if bit >> i & 1:
                count += 1
                for j in range(i+1,N):
                    if bit >> j & 1:
                        if (i,j) not in knowned:
                            flag = False
        if flag:
            ans = max(ans, count)

    print(ans)

if __name__ == '__main__':
    main()