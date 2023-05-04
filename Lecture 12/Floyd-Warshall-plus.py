# n132 
# AD 2023 May 3rd
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
def debug(s):
    print("*"*0x10)
    for x in s:
        print(x)
    print("*"*0x10)
def DP(G):
    # init the map
    # l[len(G.e)][len(G.v)][len(G.v)]
    lv = len(G.v)
    P = [[ "X" for _ in range(lv)] for __ in range(lv)]
    D = [[[ math.inf for _ in range(lv)] for __ in range(lv)] for ___ in range(lv+1)]
    for _ in range(lv):
        for __ in range(lv):
            D[0][_][__] = G.w[_][__]
            if G.w[_][__]!=math.inf and G.w[_][__]!=0:
                P[_][__] = G.v[_]
    # Start the main loop
    # debug(P)
    for v in range(1,lv+1): # L[e]
        for n in range(lv): # edge n
            for m in range(lv):
                if D[v-1][n][v-1] + D[v-1][v-1][m] < D[v-1][n][m]:
                    D[v][n][m] = D[v-1][n][v-1] + D[v-1][v-1][m]
                    P[n][m] = P[v-1][m]
                else:
                    D[v][n][m] = D[v-1][n][m]
                # D[v][n][m] = min(D[v-1][n][v-1] + D[v-1][v-1][m],D[v-1][n][m])
    debug(P)
    return D,P
if __name__ == "__main__":
    # G = GRAPH(["1","2","3","4","5","6"],[
    #     ["1","5",-1],["2","1",1],["2","4",2],
    #     ["3","2",2],["3","6",-8],["4","1",-4],
    #     ["4","5",3],["5","2",7],["6","2",5],["6","3",10]])
    G = GRAPH(["1","2","3","4","5"],[
        ["1","2",3],["1","3",8],["1","5",-4],
        ["2","4",1],["2","5",7],["3","2",4],
        ["4","1",2],["4","3",-5],["5","4",6],])
    D,P = DP(G)
    for x in D[-1:]:
        for l in x:
            print(l)
        print("="*0x10)
    print("")
    # for x in P:
        # print(x)
    # print(P)