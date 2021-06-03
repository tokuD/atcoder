from itertools import permutations
N = int(input())
a = [int(input()) for _ in range(N)]
ans = -1
count = 0
on = 1
LoopCheck = []
for _ in range(N):
    on = a[on-1] #! ボタン押す
    count += 1
    if on == 2:
        ans = count
        break

print(ans)
