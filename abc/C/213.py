H,W,N = map(int,input().split())
AB = [list(map(int,input().split())) for i in range(N)]
a = []
b = []
ans = [(0,0) for i in range(N)]
for i in range(N):
    a.append((AB[i][0],i))
    b.append((AB[i][1],i))

a.sort()
b.sort()

row = 0
columns = 0
pre_x = 0
pre_y = 0

for i in range(N):
    n = a[i][1]
    m = b[i][1]
    if i == 0:
        row = 1
        columns = 1
    elif a[i-1][0] == a[i][0] and b[i-1][0] == b[i][0]:
        row = pre_x
        columns = pre_y
    elif a[i-1][0] == a[i][0]:
        row = pre_x
        columns = pre_y + 1
    elif b[i-1][0] == b[i][0]:
        row = pre_x + 1
        columns = pre_y
    else:
        row = pre_x + 1
        columns = pre_y + 1
    AB[n][0] = row
    AB[m][1] = columns
    pre_x = row
    pre_y = columns


for i in range(N):
    print(AB[i][0], AB[i][1])
