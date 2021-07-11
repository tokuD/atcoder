N = int(input())
a = int(N  * 1.08)
ans = ':('
if a < 206:
    ans = 'Yay!'
elif a == 206:
    ans = 'so-so'
print(ans)
