def fun(a):
    i=0
    c=1
    while i<len(a):
        if a[i]==a[-1]:
            c+=1
        i+=1
    print(c)
fun(['abc', 'xyz', 'aba', '1221'])
