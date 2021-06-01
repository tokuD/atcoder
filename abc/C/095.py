A, B, C, X, Y = map(int, input().split())
ans = 0

#! 全部A,B単体で買う
if 2*C > A+B:
    ans = A*X + B*Y
#! ABも買う
else:
    #! Aピザの方が多いとき、ABピザはY枚だけ買う
    if X >= Y:
        ans += 2*C*Y
        #! Aピザ単体よりABピザを買った方が安いとき
        if 2*C <= A:
            ans += 2*C*(X-Y)
        else:
            ans += A*(X-Y)
    #! Bピザの方が多いとき
    else:
        ans += 2*C*X
        if 2*C <= B:
            ans += 2*C*(Y-X)
        else:
            ans += B*(Y-X)
print(ans)
