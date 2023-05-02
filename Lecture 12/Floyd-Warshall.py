# n132 
# AD 2023 May 2nd
# Brooklyn, NY

import math 
class GRAPH():
    def __init__(self,v,e) -> None:
        self.w = [[math.inf for __ in range(len(v))] for _ in range(len(v))]
        for x in v:
            for y in e:
                if x == y[0]:
                    i1 = v.index(y[0])
                    i2 = v.index(y[1])
                    self.w[i1][i2] = y[2]
        for x in range(len(v)):
            self.w[x][x] = 0 
        self.v = v
        self.e = e
    def W(self,a,b):
        return self.w[self.v.index(a)][self.v.index(b)]
    
def DP(G):
    # init the map
    # l[len(G.e)][len(G.v)][len(G.v)]
    lv = len(G.v)
    D = [[[ math.inf for _ in range(lv)] for __ in range(lv)] for ___ in range(lv+1)]
    for _ in range(lv):
        for __ in range(lv):
            D[0][_][__] = G.w[_][__]

    # Start the main loop
    for v in range(1,lv+1): # L[e]
        for n in range(lv): # edge n
            for m in range(lv):
                D[v][n][m] = min(D[v-1][n][v-1] + D[v-1][v-1][m],D[v-1][n][m])
    return D[-1]
if __name__ == "__main__":
    G = GRAPH(["1","2","3","4","5"],[
        ["1","2",3],["1","3",8],["1","5",-4],
        ["2","4",1],["2","5",7],["3","2",4],
        ["4","1",2],["4","3",-5],["5","4",6],])
    res = DP(G)
    for x in res:
        print(x)