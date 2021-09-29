A,B = map(int,input().split())

t_min = 1 * A
t_max = 6 * A

if t_min <= B <= t_max:
    print('Yes')
else:
    print('No')
