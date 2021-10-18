from typing import List

class Edge():

    def __init__(self, _id:int, node:List[Node]):
        self.id = _id #* 辺番号
        self.node:List[Node] = node #* この辺がつないでいる頂点


class Node():

    def __init__(self, _id:int):
        self.id = _id #* 頂点番号
        self.c = 0 #* 書かれている整数
        self.edge:List[Edge] = [] #* 辺

