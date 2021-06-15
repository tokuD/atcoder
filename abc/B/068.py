N = int(input())
num = 0
ans = 0

if N == 1:
    print(1)
    exit()

for i in range(1,N+1):
    j = i
    count = 0
    while i % 2 == 0:
        i /= 2
        count += 1
    if count > num:
        ans = j
        num = count
print(ans)
