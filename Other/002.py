N,P = map(int, input().split())
mod = 10**9+7

ans = (P-1) % mod
ans *= pow(P-2,N-1,mod)
ans %= mod
print(ans)