# 1 to 1000 perfect number in function 

def prefect():
    n=1
    while n<=1000:
        i=1
        sum=0
        while i<n:
            if n%i==0:
                sum+=i
            i+=1  
        if sum==n:
            print(n)
        n=n+1
prefect()

# how to find which number is perfect number hain?

def prefect(num):
    i=1
    sum=0
    while i<num:
        if num%i==0:
            sum+=i
        i+=1
    return sum==i
p=prefect(int(input("enter a number :")))
print(p) 