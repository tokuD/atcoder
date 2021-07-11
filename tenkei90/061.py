from collections import deque
Q = int(input())
# top = []
# bottom = []
mount = deque()
for i in range(Q):
    t,x = map(int,input().split())
    if t == 1:
        # top.append(x)
        mount.appendleft(x)
    elif t == 2:
        # bottom.append(x)
        mount.append(x)
    else:
        # if x <= len(top):
        #     print(top[-x])
        # else:
        #     x -= len(top)
        #     print(bottom[x-1])
        print(mount[x-1])
