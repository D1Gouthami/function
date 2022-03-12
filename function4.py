def fun(a):
    i=0
    c=0
    min=a[i]
    while i<len(a):
        if a[i]<min:
            min=a[i]
            c+=1
        i+=1
    print(min)
fun([8,6,4,8,4,50,2,7])