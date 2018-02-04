
def multi(n):
    list1 =[]
    list2 =[]
    for i in range(1,n+1):
        for k in range(i,(i*i)+1 ,i):
            list1.append(k)
        list2.append(list1)
        list1 = []
    return list2
