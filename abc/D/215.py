import math
import numpy as np

"""nを素因数分解"""
def factorization(n,ans):
    temp = n
    flag = True
    for i in range(2,int(math.sqrt(n)+2)):
        if temp % i == 0:
            flag = False
            temp = temp//i
            ans.add(i)
    if flag:
        ans.add(n)



def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    ans = [1]
    A = np.array(A)
    # s = 1
    # ans = {1}
    # f_ans = [1]

    # for i in range(N):
    #     factorization(A[i],ans)

    for i in range(2,M+1):
        a = np.array([i])
        a.repeat(N)
        if np.gcd(a,A) == np.ones(N):
            ans.append(i)

    print(len(ans))
    for i in ans:
        print(ans)

    # print(len(f_ans))
    # for a in f_ans:
    #     print(a)



if __name__ == '__main__':
    main()
