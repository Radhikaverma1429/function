def sum(a,b,c):
    if a>b or a>c:
        print("a is greaterthen b and c")
    elif b>a and b>c:
        print("b is greterthen a and c")
    elif c>a and c>b:
        print("c is greterthen a and b")
    else:
        print("this are equal")
sum(a=int(input(" enter a number :")),b=int(input("enter a number :")),c=int(input("enter a number :"))
)   