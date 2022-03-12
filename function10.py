def add(a,b):
    c=a+b
    return c
def sub(x,y):
    z=x-y 
    return z
def mult(g,e):
    d=e*g
    return d
def div(r,q):
    m=r//q
    return m
def main():
    if optn=="+":
        print(add(num1,num2))
    elif optn=="-":
        print(sub(num1,num2)) 
    elif optn=="*":
        print(mult(num1,num2)) 
    elif optn=="//":
        print(div(num1,num2)) 
    else:
        print("nothing")    
    num1=int(input("enter the num"))
    num2=int(input("enter the num"))
    optn=input("enter operator")
main()                




    
    
