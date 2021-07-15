import math

def main():
    T = int(input())
    L,X,Y = map(int,input().split())
    Q = int(input())
    E = [int(input()) for i in range(Q)]

    for t in E:
        theta = 2*math.pi*t/T
        y = -L/2*math.sin(theta)
        z = L/2*(1-math.cos(theta))
        ans = math.atan(z/math.sqrt(X**2+(Y-y)**2))
        print(math.degrees(ans))

if __name__ == '__main__':
    main()
