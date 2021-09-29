N = int(input())
ST = [input() for _ in range(N)]
st = set(ST)

if len(st) == N:
    print('No')
else:
    print('Yes')
