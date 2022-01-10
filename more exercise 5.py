def factoriol(num):
    i=1
    sum=0
    while i<=num:
        if num%i==0:
            sum+=i
            i+=1
        return sum==i
    print(sum)
factoriol(int(input("enter a number :")))
