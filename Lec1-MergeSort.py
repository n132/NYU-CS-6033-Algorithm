def merge(a,b):
    res= [] 
    while(a!=[] and b!=[]):
        if a[-1] <= b[-1]:
            res.append(b.pop())
        else:
            res.append(a.pop())
    res += a[::-1] if b==[] else b[::-1]
    return res[::-1]
        
def merge_sort(a):
    if len(a)==1:
        return a
    mid = int(len(a)//2)
    b = merge_sort(a[:mid])
    c = merge_sort(a[mid:])
    return merge(b,c)

if __name__ == "__main__":
    res = merge_sort([5,3,4,2,1])
    print(res)