N = int(input())
#* city[i]:[合計、青木派、高橋派]
city = []
aoki = 0
takahashi = 0
for _ in range(N):
    a,b = map(int, input().split())
    city.append([2*a+b,a,b])
    aoki += a

city.sort(key=lambda x:x[0], reverse=True)
ans = 0
for i in range(N):
    s,a,t = city[i]
    takahashi += s
    if aoki < takahashi:
        ans = i+1
        break
print(ans)
