N = int(input())
ans = []

while True:
    if N == 1:
        ans.append('A')
        break
    if N % 2 == 0:
        N //= 2
        ans.append('B')
    else:
        N -= 1
        ans.append('A')

a = len(ans)
for i in range(1,a)[::-1]:
    print(ans[i],end='')

print(ans[0])
