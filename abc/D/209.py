N,Q = map(int,input().split())
load = [[] for i in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    load[a-1].append(b)
for i in range(Q):
    c,d = map(int,input().split())

print(load)
