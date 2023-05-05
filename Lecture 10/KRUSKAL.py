class node():
    def __init__(self,note,parent =None, rank=0) -> None:
        self.r = rank
        self.note = note
        if parent:
            self.p = parent
        else:
            self.p = self
class Nset():
    def __init__(self) -> None:
        pass
        self.db = []
    def makeset(self,x):
        self.db.append(node(x,None,0))
    def union(self,x,y):
        s1 = self.findset(x)
        s2 = self.findset(y)
        if s1==s2:
            return
        if s1.r >s2.r:
            s2.p = s1.p
        elif s1.r<s2.r:
            s1.p = s2.p
        else:
            s2.p = s1.p
            s1.r+=1
        
        return 
    def findset(self,x):
        if x.__class__ != "".__class__:
            while x!=x.p:
                x = x.p
            return x.p
        else:
            for i in self.db:
                if i.note == x:
                    return self.findset(i)
        raise Exception(f"Can't Find the Item {x}")

def KRUSKAL(Gv,w):
    res = []
    db = Nset()
    for x in Gv:
        db.makeset(x)
    def cmp(s):
        return s[2]
    w.sort(key=cmp)
    for u,v,_ in w:
        U = db.findset(u)
        V = db.findset(v)
        if U != V:
            db.union(U,V)
            res.append((u,v))
    return res
if __name__ =="__main__":
    w = [
        ('f','c',3),
        ('f','i',3),
        ('u','c',3),
        ('b','c',6),
        ('i','b',5),
        ('c','e',4),
        ('e','u',1),
        ('u','b',4),
        ('u','v',2),
        ('d','v',2),
        ('b','d',1),
        ('d','g',3),
        ('v','g',5),]
    Gv = ['f','c','i','e','u','b','d','v','g']
    res = KRUSKAL(Gv,w)
    print(res)
    print(len(res))