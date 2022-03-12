def cheak_number_list():
    a=[2, 6, 18, 10, 3, 75] 
    b=[6, 19, 24, 12, 3, 87]
    i=0
    while i<len(a):
        if b[i]%2==0:
            print("even")
        else:
            print("odd")
        i+=1
cheak_number_list()