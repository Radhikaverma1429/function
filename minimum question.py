def min_fun(a):
    i=0
    b=(a[i])
    while i<len(a):
        if a[i]<b:
            b=a[i]
        i+=1
    print(b) 
min_fun(a = [8, 6, 4, 8, 4, 50, 2, 7]) 
