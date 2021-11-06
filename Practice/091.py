#from __future__ import annotations
from typing import List,Union
import sys
input = sys.stdin.readline
# from collections import defaultdict,deque
# from itertools import permutations,combinations
# from bisect import bisect_left,bisect_right
# import heapq
# sys.setrecursionlimit(10**5)
from math import sin,cos,tan,pi

def rad(theta):
    return theta * pi / 180

def main():
    a,b,x = map(int,input().split())
    ok = 0
    ng = 90
    while abs(ok-ng) > (10**-7):
        theta = (ok+ng)/2
        alpha = 90 - theta
        V = 0
        if b*cos(rad(theta)) <= a*cos(rad(theta)):
            V = a*(b*cos(rad(theta)+b*sin(rad(theta)/tan(rad(alpha)))))*b*sin(rad(theta))/3
            print('--')
        else:
            V = a**2*b - a*( a*sin(rad(theta)) + a*cos(rad(theta))/tan(rad(theta)) ) * a*cos(rad(theta)) / 3
        if x <= V:
            ok = theta
        else:
            ng = theta

    print(ok)
    print(ng)


if __name__ == '__main__':
    main()