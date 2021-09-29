N = int(input())
AB = [list(map(int,input().split())) for _ in range(N)]
AB.sort(key=lambda x:x[1])
t = 0
for i in range(N):
    t += AB[i][0]
    if AB[i][1] < t:
        print('No')
        exit()

print('Yes')
