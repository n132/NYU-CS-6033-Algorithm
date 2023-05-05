
# Assume we have hw to choose: [1,23123,1231,23]
# We can only chose the first/last one
# chose the hw needs shortest time
def DP(Q):
    return min(Q) if len(Q) <= 2 else min(sum(Q[1:])-DP(Q[1:])+Q[0],sum(Q[:-1])-DP(Q[:-1])+Q[-1])

if __name__ == "__main__":
    print(DP([100,3,100,3]))