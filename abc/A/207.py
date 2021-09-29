ABC = list(map(int,input().split()))
total = sum(ABC)
ans = []
for i in range(3):
    ans.append(total - ABC[i])

print(max(ans))
