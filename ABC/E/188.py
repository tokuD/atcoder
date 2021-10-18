from typing import List
N,M = map(int, input().split())
A = list(map(int, input().split()))
INF = 10**20

class Node():
    def __init__(self, num:int):
        self.num = num
        self.child:List[Node] = []
        self.price = A[num]
        self.buy = INF #* 今まで通ってきた経路での最安値

    def profit(self):
        return self.price - self.buy

nodes:List[Node] = [Node(i) for i in range(N)]
for _ in range(M):
    x,y = map(lambda x:int(x)-1, input().split())
    nodes[x].child.append(nodes[y])

ans = -INF

#* 配るdp
for node in nodes:
    for child in node.child:
        child.buy = min(child.buy,node.buy, node.price)
    ans = max(ans,node.profit())

print(ans)