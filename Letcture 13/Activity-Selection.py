def Activity_Selection(E):
    def cmp(a):
        return a[1]
    E.sort(key=cmp)
    res = []
    while(len(E)!=0):
        res.append(E[0])
        E.remove(E[0])
        for x in E:
            if x[0] < res[-1][1]:
                E.remove(x)
    return res
if __name__ == "__main__":
    E = [[1,23],[2,4],[13,15],[4,17],[8,9]]
    print(Activity_Selection(E))
