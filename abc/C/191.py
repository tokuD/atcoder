from typing import List
import sys
sys.setrecursionlimit(10**6)
H,W = map(int, input().split())
S = [list(input()) for _ in range(H)]
S1 = [['.']*W for _ in range(H)]
start = []
for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            continue
        if S[i+1][j] == '#' and S[i-1][j] == '#' and S[i][j+1] == '#' and S[i][j-1] == '#':
            continue
        S1[i][j] = '#'
        if len(start) == 0:
            start.append(i)
            start.append(j)

visited = [[False]*W for _ in range(H)]
command = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
ans = 0
def dfs(curr: List[int], direction: List[int] = None):
    i,j = curr
    for co in command:
        di,dj = co
        if S1[i+di][j+dj] == '#':
            if visited[i+di][j+dj]:
                continue
            if direction == None:
                direction = co
            else:
                visited[i+di][j+dj] = True
                if co != direction:
                    global ans
                    ans += 1
                    direction = co
                    print(i+di,j+dj)
            dfs([i+di,j+dj],direction)

dfs(start)

print(ans)
print(start)