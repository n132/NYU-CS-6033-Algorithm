def Activity_Selection(E):
    def cmp(a):
        return a[0]
    E.sort(key=cmp)
    res = []
    while(len(E)!=0):
        res.append(E.pop())
        for x in E[::-1]:
            if x[1] > res[-1][0]:
                E.remove(x)
    return res
if __name__ == "__main__":
    E = [[1,23],[2,4],[13,15],[4,17],[8,9]]
    print(Activity_Selection(E))
