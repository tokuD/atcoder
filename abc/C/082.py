N = int(input())
a = list(map(int,input().split()))
a.sort()
now_num = a[0]
count = 1
ans = 0
# print(a)
for i in range(1,N):
    if now_num == a[i]:
        count += 1
    else:
        if count >= now_num:
            ans += count - now_num
            # print(count,now_num)
        else:
            ans += count
            # print(count)
        now_num = a[i]
        count = 1

if count >= now_num:
    ans += count - now_num
else:
    ans += count

print(ans)
