def fun_num(l1,l2):
    i=0
    sum=0
    empty=[]
    while i<(l1):
        j=0
        while j<(l2):
            if (l1)==(l2):
                sum=sum+l1[i][j]
                empty.append(sum)
            j+=1
        i+=1
    print(empty)
fun_num(int(input("enter a number ")),int(input("enter a number "))) 