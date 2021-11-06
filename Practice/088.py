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
    N = int(input())
    stack = deque()
    #* [個数,色]
    stack.append([0,0])
    for i in range(1,N+1):
        c = int(input())
        if i % 2 == 1:
            l = stack.pop()
            if l[1] == c:
                stack.append([l[0]+1,c])
            else:
                stack.append(l)
                stack.append([1,c])
        else:
            l = stack.pop()
            if l[1] == c:
                stack.append([l[0]+1,c])
            else:
                if len(stack)>0:
                    l1 = stack.pop()
                    stack.append([l[0]+l1[0]+1,c])
                else:
                    stack.append([l[0]+1,c])

    ans = 0
    while len(stack) > 0:
        l = stack.pop()
        if l[1] == 0:
            ans += l[0]

    print(ans)

if __name__ == '__main__':
    main()