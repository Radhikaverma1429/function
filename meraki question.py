def fun_name(n,m):
    if len(n)>len(m):
        print(n)
    elif len(m)>len(n):
        print(m)
    else:
        print(m,n)
fun_name(input("enter a value :"),input("enter a value :"))