N = int(input())
s = [list(input().rstrip()) for _ in range(N)]
ans = 0
for i in range(N):
    s[i] = sorted(s[i])
s.sort()
count = 1
now_char = s[0]
for i in range(1,N):
    """i文字目とi-1文字目を比較し、同じならans += 1,違ったらnow_charを更新"""
    if now_char == s[i]:
        count += 1
    else:
        ans += count * (count-1) // 2
        count = 1
        now_char = s[i]
ans += count * (count-1) // 2

print(ans)
