from traceback import print_tb


N,K = map(int, input().split())
N %= K
kisyutu = [N]

while True:
    N = abs(N-K)
    if N in kisyutu:
        break
    kisyutu.append(N)

kisyutu.sort()
print(kisyutu[0])
