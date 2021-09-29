from unittest.util import unorderable_list_difference
from numpy import union1d


class Union_Find():
    def __init__(self,N):
        """N:頂点数"""
        self.par = [-1] * N #*各頂点の親の番号を格納する。自身が根の時は-1を格納
        self.siz = [1] * N #*各頂点の属する根付き木の頂点数を表す。

    def root(self,x):
        """要素xを含むグループ(根付き木)の根を返すメソッド ※計算量はO(h) h:根付き木の高さ
        """
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def issame(self,x,y):
        """root(x)とroot(y)が等しいかどうかを判定する"""
        return self.root(x) == self.root(y)

    def unite(self,x,y):
        """root(x)がroot(y)の子頂点となるようにつなぐ
        頂点数の少ない方の木を、大きい方につける
        """
        x,y = self.root(x),self.root(y) #* xyを根まで移動する
        if x == y:
            return #*すでに根が同じ時は何もしない
        x,y = max(x,y),min(x,y) #* yの方がサイズが小さくなるように交換
        self.par[y] = x #* yをxの子にする
        self.siz[x] += self.siz[y]
        return

    def size(self,x):
        """xを含む木のサイズを返す"""
        return self.siz[x]

def main():
    H,W = map(int,input().split())
    Q = int(input())
    q_list = [list(map(int,input().split())) for _ in range(Q)]
    union_find = Union_Find(H*W)
    F = [[0 for j in range(W)] for i in range(H)]
    for i in range(Q):
        q = q_list[i]
        if q[0] == 1:
            r,c = map(lambda x:x-1,q[1:])
            F[r][c] = 1
            # print(r,c)
            if 0 <= r <= H-1 and 0<= c-1 <= W-1:
                if F[r][c-1] == 1:
                    union_find.unite(r*W+c,r*W+c-1)
            if 0 <= r <= H-1 and 0<= c+1 <= W-1:
                if F[r][c+1] == 1:
                    union_find.unite(r*W+c,r*W+c+1)
            if 0 <= r-1 <= H-1 and 0<= c <= W-1:
                if F[r-1][c] == 1:
                    union_find.unite(r*W+c,(r-1)*W+c)
            if 0 <= r+1 <= H-1 and 0<= c <= W-1:
                if F[r+1][c] == 1:
                    union_find.unite(r*W+c,(r+1)*W+c)
        else:
            ra,ca,rb,cb = map(lambda x:x-1,q[1:])
            x = ra*W + ca
            y = rb*W + cb
            if union_find.issame(x,y):
                print('Yes')
            else:
                print('No')




if __name__ == '__main__':
    main()
