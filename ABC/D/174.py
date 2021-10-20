from collections import deque

def main():
    N = int(input())
    C = list(input())
    R = deque() #* stack
    W = deque() #* que
    for i in range(N):
        c = C[i]
        if c == 'W':
            W.append(i)
        else:
            R.append(i)

    ans = 0

    while len(R) > 0 and len(W) > 0:
        r = R.pop()
        w = W.popleft()
        if w < r:
            ans += 1
        else:
            break

    print(ans)


if __name__ == '__main__':
    main()