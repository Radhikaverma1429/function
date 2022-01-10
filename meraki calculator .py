def calculator(num_x,num_y,opration):
    if opration=="+":
        return num_x+num_y
    elif opration=="*":
        return num_x*num_y
    elif opration=="-":
        return num_x-num_y
    elif opration=="/":
        return num_x/num_y
    elif opration =="%":
        return num_x%num_y
    elif opration=="**":
        return num_x**num_y
    else:
        return num_x//num_y
print(calculator(num_x=int(input("enter a number :")),num_y=int(input("enter anumber :"))
,opration=input("enter a symbals :"))) 



