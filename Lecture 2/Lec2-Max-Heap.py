import math
class MAX_HEAP(object):
    def __init__(self,data = []) -> None:
        self.tree = data
    def HEAP(self):
        return self.tree
    def PARENT(self,i):
        assert(i<len(self.tree))
        if i == 0:
            return 0
        return int((i-1)//2)
    def LEN(self):
        return len(self.tree)
    def LEFT(self,i):
        assert(i*2+1<len(self.tree))
        return self.tree[i*2+1]
    def RIGHT(self,i): # O(1)
        print(i*2+2,i)
        assert(i*2+2<len(self.tree))
        return self.tree[i*2+2]
    def HEIGHT(self): # O(1) Assume me have a counter
        l = self.LEN()
        if l == 0:
            return 0
        return int(math.log2(l)+1)
    def MAXUNUM(self): # O(1)
        assert(len(self.tree)>0)
        return self.tree[0]
    def EXTRACT_MAX(self): # log(n)
        res = self.MAXUNUM()
        self.tree[0] = self.tree.pop()
        self.MAX_HEAPIFY(0)
        return res
    def INSERT(self,key):# log(n)
        self.tree.append(-math.inf)
        self.INCREASE_KEY(len(self.tree)-1,key)
        return 
    def EXCHANGE(self,i1,i2):# O(1)
        assert(i1<len(self.tree))
        assert(i2<len(self.tree))
        tmp = self.tree[i1]
        self.tree[i1] = self.tree[i2]
        self.tree[i2] = tmp
        return
    def INCREASE_KEY(self,i,key): # log(n) 
        assert(i<self.LEN())
        self.tree[i]  = key
        while i!=0 and key > self.tree[self.PARENT(i)]:
            self.EXCHANGE(self.PARENT(i),i)
            i = self.PARENT(i)
        return 
    def BUILD_MAX_HEAP(self):# O(n)
        if self.LEN() <=1:
            return 
        h = 2**(self.HEIGHT()-1)-1
        for x in range(h,-1,-1):
            self.MAX_HEAPIFY(x)
        return 
    def MAX_HEAPIFY(self,i):# log(n) 
        r = (i+1)*2 
        l = (i+1)*2-1
        if  l < self.LEN() and self.tree[i] < self.tree[l]:
            smallest = l
        else:
            smallest = i
        if r < self.LEN()  and self.tree[smallest] < self.tree[r]:
            smallest = r
        if i!=smallest:
            self.EXCHANGE(i,smallest)
            self.MAX_HEAPIFY(smallest)
        return 
def HEAP_SORT(array):# nlog(n)
    h = MAX_HEAP(array)
    h.BUILD_MAX_HEAP()
    res = []
    for _ in range(h.LEN(),0,-1):            
        h.EXCHANGE(0,h.LEN()-1)
        res.append(h.tree.pop())
        h.MAX_HEAPIFY(0)
    return res
# h = HEAP_SORT([5,4,3,1,2,8,9,0][::-1])
# print(h)
h = MAX_HEAP([-2,6,3,11,2,4])
h.BUILD_MAX_HEAP()
h.EXTRACT_MAX()
h.INSERT(56)
res = h.HEAP()
print(res)

