class node(object):
    def __init__(self, k, n,parent=None,l = None,r=None) -> None:
        self.left  = l
        self.right = r
        self.key = k
        self.note = n  
        self.p = parent
import math
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
    def INSERT(self,x):# log(n)
        self.tree.append(node(math.inf,x.note,x.p,x.left,x.right))
        self.DECREASE_KEY(len(self.tree)-1,x.key)
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
    
def HUFFMAN(key):
    tmp = []
    for x in key:
        tmp.append(node(x[1],x[0]))
    Q = PQ(tmp)
    n = len(key)
    x = None
    for _ in range(n-1):
        x = node(0,"")
        x.left = Q.EXTRACT_MIN()
        x.right = Q.EXTRACT_MIN()
        x.left.p = x.right.p = x
        x.key = x.left.key + x.right.key
        Q.INSERT(x)
    t = Q.EXTRACT_MIN()
    return t

def travel(root):
    if root!=None:
        print(root.key,root.note)
        travel(root.left)
        travel(root.right)
if __name__ == "__main__":
    key = [
        ["Z",2],
        ["K",7],    
        ["M",24],
        ["C",32],
        ["U",37],
        ["D",42],
        ["L",42],
        ["E",120],
    ]
    tree = HUFFMAN(key)
    travel(tree)
