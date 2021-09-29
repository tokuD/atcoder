N = int(input())
x = []
y = []

for i in range(N):
    xi,yi = map(int,input().split())
    x.append(xi)
    y.append(yi)

x.sort()
y.sort()

samex = []
nowx = x[0]
countx = 1
samey = []
nowy = y[0]
county = 1
for i in range(1,N):
    if nowx == x[i]:
        countx += 1
    else:
        if countx>1:
            samex.append(countx)
        nowx = x[i]
        countx = 1
    if nowy == y[i]:
        county += 1
    else:
        if county>1:
            samey.append(county)
        nowy = y[i]
        county = 1

if countx > 1:
    samex.append(countx)
if county > 1:
    samey.append(county)

