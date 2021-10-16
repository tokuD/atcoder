V,T,S,D = map(int, input().split())

if V*T <= D <= S*V:
    print('No')
else:
    print('Yes')