N,A,B = list(map(int, input().split()))
ans = 0
for nums in range(1, N+1):
    total = 0
    for num in list(str(nums)):
        total += int(num)
    if total >= A and total <= B:
        ans += nums
print(ans)