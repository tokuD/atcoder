
def Eratosthenes(N):
    """1~Nで素数を探す"""
    isprime = [True]*(N+1)
    isprime[0],isprime[1] = False,False
    for i in range(2,N+1):

        #* iが素数でない場合
        if not isprime[i]:
            continue

        #* iが素数なら、i以外のiの倍数をふるい落とす
        for j in range(2*i,N+1,i):
            isprime[j] = False

    #* isprime[i]:iが素数ならTrue
    return isprime
