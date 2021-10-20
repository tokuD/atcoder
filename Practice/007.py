from itertools import combinations

def main():
    n = int(input())
    cur = [tuple(map(int,input().split())) for _ in range(n)]

    XY = set(cur)
    ans = 0

    for (x0,y0), (x1,y1) in combinations(cur,2):
        dx = x1 - x0
        dy = y1 - y0
        if (x1+dy,y1-dx) not in XY:
            continue
        if (x0+dy,y0-dx) not in XY:
            continue
        ans = max(ans, dx**2 + dy**2)

    print(ans)

if __name__ == '__main__':
    main()