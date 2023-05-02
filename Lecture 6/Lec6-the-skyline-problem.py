class Solution(object):
    def combine(self,L,R):
        
        # Combine ? and nothing
        
        if len(L)==0 or len(R) == 0:
            return L if len(R) == 0 else R
        res = []
        p1 = p2 = 0
        cur = 0  # current height
        dom = -1 # dominator
        # init cur and dom
        if(L[p1][0]<R[p2][0]):
            res.append(L[p1])
            cur = L[p1][1]
            p1 +=1
            dom = "L"
        elif(L[p1][0]>R[p2][0]):
            res.append(R[p2])
            cur = R[p2][1]
            p2 += 1
            dom = "R"
        else:
            bigger = L[p1][1] if  L[p1][1] > R[p2][1] else R[p2][1]
            bigger_side = "L" if  L[p1][1] > R[p2][1] else "R"
            if cur!=bigger:
                res.append([L[p1][0],bigger])
            cur =  bigger
            dom =  bigger_side
            p1+=1
            p2+=1
        while p1<len(L) and p2 < len(R):
            if(L[p1][0] < R[p2][0]):# next on x
                if ( L[p1][1] > cur): # higer than current height
                    res.append(L[p1])
                    cur = L[p1][1]
                    dom = "L"
                elif( L[p1][1] < cur): # 
                    if dom=="L":
                        if p2>0 and R[p2-1][1] > L[p1][1]:# todo what if the same
                            res.append([L[p1][0],R[p2-1][1]])
                            cur= R[p2-1][1]
                            dom = "R"
                        else:
                            res.append(L[p1])
                            cur = L[p1][1]
                            dom = "L"
                    else:
                        pass
                else:
                    dom = "L"
                p1+=1
            elif(L[p1][0] > R[p2][0]):# next on x
                if ( R[p2][1] > cur): # higer than current height
                    res.append(R[p2])
                    cur = R[p2][1]
                    dom = "R"
                elif( R[p2][1] < cur): # 
                    if dom=="R":
                        if p1>0 and R[p2][1] < L[p1-1][1]:# todo what if the same
                            res.append([R[p2][0],L[p1-1][1]])
                            cur= L[p1-1][1]
                            dom = "L"
                        else:
                            res.append(R[p2])
                            cur =R[p2][1]
                            dom = "R"
                    else:
                        pass
                else:
                    dom = "R"
                p2+=1
            else:
                bigger = L[p1][1] if  L[p1][1] > R[p2][1] else R[p2][1]
                bigger_side = "L" if  L[p1][1] > R[p2][1] else "R"
                if cur!=bigger:
                    res.append([L[p1][0],bigger])
                cur =  bigger
                dom =  bigger_side
                p1+=1
                p2+=1
        # Return the result
        if p1 == len(L):
            res+=R[p2:]
        elif p2 == len(R):
            res+=L[p1:]
        else:
            print("Panic")
            exit(1)
        return res
    def getSkyline(self, buildings):
        # print(buildings)
        if len(buildings) == 1:
            ele = buildings[0]
            return [[ele[0],ele[2]],[ele[1],0]]
        L = self.getSkyline(buildings[:int(len(buildings)/2)])
        R = self.getSkyline(buildings[int(len(buildings)/2):])
        return self.combine(L,R)
if __name__ == "__main__":
    s = Solution()
    res = s.getSkyline([[4,9,10],[4,9,15],[4,9,12],[10,12,10],[10,12,8]])
    print(res)