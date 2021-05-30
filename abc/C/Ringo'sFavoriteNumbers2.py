N = int(input())
A = list(map(int, input().split()))
ans = 0

A = list(map(lambda x:x%200, A))
amari = [0 for i in range(200)] #! amaris[i]は余りがiになるAの数

for a in A:
    amari[a] += 1

# print(amari)
ans = 0
for n in amari:
    ans += int(n * (n-1) / 2)

print(ans)
