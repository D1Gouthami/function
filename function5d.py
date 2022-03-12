def fun(a):
    i=0
    b=[]
    while i<len(a):
        if a[i] not in b:
            b.append(a[i])
        i+=1
    print(b)
fun([1,1,2,2,3,3,9,9])
    
