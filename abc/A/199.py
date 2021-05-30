A, B, C = map(int, input().split())

def judge(a, b, c):
    if a**2 + b**2 < c**2:
        return "Yes"
    else:
        return "No"

print(judge(A, B, C))
