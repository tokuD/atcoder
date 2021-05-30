N = int(input())
ans = 0

def judge(i):
    return not(len(str(i)) % 2 == 0)

for i in range(1, N+1):
    if judge(i):
        ans += 1

print(ans)
