import sys
sys.setrecursionlimit(10**6)

N = int(input())
H = list(map(int,input().split()))

cost = [0]*N
flag = [False]*N
cost[0] = 0
flag[0] = True
cost[1] = abs(H[1]-H[0])
flag[1] = True

def calc(i):
    if flag[i]:
        return cost[i]
    a = min(calc(i-1)+abs(H[i]-H[i-1]),calc(i-2)+abs(H[i]-H[i-2]))
    cost[i] = a
    flag[i] = True
    return a

print(calc(N-1))