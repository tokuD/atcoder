A,B,C = map(int, input().split())

if C == 0:
    while A > 0 and B > 0:
        A -= 1
        B -= 1
    if A == 0:
        print('Aoki')
    else:
        print('Takahashi')
else:
    while A > 0 and B > 0:
        A -= 1
        B -= 1
    if B == 0:
        print('Takahashi')
    else:
        print('Aoki')
