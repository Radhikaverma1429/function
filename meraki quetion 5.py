def limit(n):
    i=1
    sum=0
    while i<=n:
        if i%3==0:
            print(i,"divisible hai")
            sum=sum+i
        elif i%5==0:
            print(i,"divisible hai")
            sum=sum+i
        i+=1
    print(sum)
limit(10) 