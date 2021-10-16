import heapq
N = int(input())
day = []

for i in range(N):
    a,b = map(int, input().split())
    day.append([a,0])
    day.append([a+b,1])

#*  0:in 1:out
day.sort(key=lambda x: (x[0],x[1]))
ans = [0]*(N+1)
k = 0
last = 1
flag = True
#* n:日付、f:出たか入ったか
for n,f in day:
    r = n - last
    if flag:
        ans[k] += r
    if f == 0:
        k += 1
    elif f == 1:
        k -= 1
    # if day[i] == day[i+1]:
    #     flag = False
    # else:
    #     flag = True
    last = n

a = list(map(str,ans))
print(' '.join(a[1:]))