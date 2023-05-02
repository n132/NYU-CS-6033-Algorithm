# n132 
# AD 2023 May 2nd
# Brooklyn, NY

import math 
class GRAPH():
    def __init__(self,v,e) -> None:
        # Build ADJ 
        self.adj = {}
        for x in v:
            if x not in self.adj.keys():
                self.adj[x] = []
            for y in e:
                if x == y[0]:    
                   self.adj[x].append(y[1])
        self.v = v
        self.e = e

    def W(self,case):
        for i in range(len(self.e)):
            if  case == self.e[i][:2]:
                return self.e[i][2]
        return None
class node(object):
    def __init__(self, k, n,parent) -> None:
        # self.left  = l
        # self.right = r
        self.k = k
        self.note = n  
        self.p = parent

class PQ():
    # priority queue
    def __init__(self,data = []) -> None:
        self.tree = data
        self.BUILD_MIN_HEAP()
    def FIND(self,note):

        for x in self.tree:
            if x.note == note:
                return x
        return None
    def PARENT(self,i):
        assert(i<len(self.tree))
        if i == 0:
            return 0
        return int((i-1)//2)
    def HEIGHT(self): # O(1) Assume me have a counter
        l = len(self.tree)
        if l == 0:
            return 0
        return int(math.log2(l)+1)
    def MINUNUM(self): # O(1)
        assert(len(self.tree)>0)
        return self.tree[0]
    def EXTRACT_MIN(self): # log(n)
        res = self.MINUNUM()
        if len(self.tree) > 1:

            self.tree[0] = self.tree.pop()
            self.MIN_HEAPIFY(0)
        else:
            res = self.tree.pop()
        return res
    def INSERT(self,key,note,parent):# log(n)
        self.tree.append(node(math.inf,note,parent))
        self.DECREASE_KEY(len(self.tree)-1,key)
        return 
    def EXCHANGE(self,i1,i2):# O(1)
        assert(i1<len(self.tree))
        assert(i2<len(self.tree))
        tmp = self.tree[i1]
        self.tree[i1] = self.tree[i2]
        self.tree[i2] = tmp
        return
    def DECREASE_KEY(self,i,key): # log(n) 
        assert(i<len(self.tree))
        self.tree[i].key  = key
        while i!=0 and key<self.tree[self.PARENT(i)].key:
            self.EXCHANGE(self.PARENT(i),i)
            i = self.PARENT(i)
        return 
    def DECREASE_KEY_by_Note(self,note,key,p):
        for i in range(len(self.tree)):
            if self.tree[i].note == note:
                self.tree[i].key = key
                self.tree[i].p = p

                while i!=0 and key<self.tree[self.PARENT(i)].key:
                    self.EXCHANGE(self.PARENT(i),i)
                    i = self.PARENT(i)
                return 
        exit(1)
    def BUILD_MIN_HEAP(self):# O(n)
        if len(self.tree) <=1:
            return 
        h = 2**(self.HEIGHT()-1)-1
        for x in range(h,-1,-1):
            self.MIN_HEAPIFY(x)
        return 
    def MIN_HEAPIFY(self,i):# log(n) 
        r = (i+1)*2 
        l = (i+1)*2-1
        if  l < len(self.tree) and self.tree[i].key > self.tree[l].key:
            smallest = l
        else:
            smallest = i
        if r < len(self.tree)  and self.tree[smallest].key > self.tree[r].key:
            smallest = r
        if i!=smallest:
            self.EXCHANGE(i,smallest)
            self.MIN_HEAPIFY(smallest)
        return 
    
def dijkstra(G,s):
    # init the queue
    Q = PQ([])
    for x in G.v:
        if x == s:
            Q.INSERT(0,x,None)
        else:
            Q.INSERT(math.inf,x,None)
    res = []
    # print(Q.tree)
    while len(Q.tree)!=0:
        # for x in range(len(Q.tree)):
            # print(Q.tree[x].key,Q.tree[x].note)
        # print("="*0x10)
        u = Q.EXTRACT_MIN()
        res.append(u)
        # print(u.note)
        for v in G.adj[u.note]:
            tmp = Q.FIND(v)
            if tmp == None:
                continue
            if G.W([u.note,v])+u.key <tmp.key:
                Q.DECREASE_KEY_by_Note(v,G.W([u.note,v])+u.key,u.note)

    return res
    # Q = PQ([5,2,3])
    # print(Q.tree)
if __name__ == "__main__":
    G = GRAPH(["A","B","C","D","E"],[
        ["A","B",1],["A","D",2],["B","E",4],
        ["C","A",10],["C","D",5],["D","A",3],
        ["D","B",9],["D","E",2],["E","B",6],
        ["E","C",7]])
    res = dijkstra(G,"C")
    for x in res:
        print(x.note,x.key,x.p)