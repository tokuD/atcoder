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
            return False #*すでに根が同じ時は何もしない
        x,y = max(x,y),min(x,y) #* yの方がサイズが小さくなるように交換
        self.par[y] = x #* yをxの子にする
        self.siz[x] += self.siz[y]
        return True

    def size(self,x):
        """xを含む木のサイズを返す"""
        return self.siz[x]
