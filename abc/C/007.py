from collections import deque

R,C = map(int,input().split())
S = list(map(int,input().split()))
G = list(map(int,input().split()))
labyrinth = [list(map(lambda x: x=='.',list(input()))) for _ in range(R)]
visited = [[False]*C for _ in range(R)] #[row][column]
to_visit = deque() #([row1,column1],[row2,column2],,)
S.append(1)
to_visit.append(map(lambda x:x-1,S))
G = list(map(lambda x:x-1,G))
ans = [[0]*C for _ in range(R)]

def query(row,column,dis):
    global to_visit,visited,ans
    if (not visited[row][column]) and (labyrinth[row][column]):
        to_visit.append([row,column,dis+1])
        visited[row][column] = True
        ans[row][column] = dis+1


while len(to_visit) > 0:
    row,column,dis = to_visit.popleft()
    query(row-1, column,dis)
    query(row+1, column,dis)
    query(row, column-1,dis)
    query(row, column+1,dis)

print(ans[G[0]][G[1]])