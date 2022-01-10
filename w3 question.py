# def mul(num):
#     i=0
#     sum=1
#     while i<len(num):
#         sum*=num[i]
#         i+=1
#     return sum
# print(mul([8,2,3,-1,7]))

# w3 quetion no 4?


# def reverse(str1):
#     rstr1 = ''
#     i= len(str1)
#     while i > 0:
#         rstr1 += str1[ i - 1 ]
#         i = i- 1
#     return rstr1
# print(reverse('1234abcd'))

# def string(str1):
#     c=0
#     c1=0
#     i=0
#     while i<len(str1):
#         if str1[i]>"A" and str1[i]<"Z":
#             c+=1
#         elif str1[i]>"a" and str1[i]<"z":
#             c1+=1
#         i+=1
#     return( c,c1)
    
# print(string(str1='The quick Brow Fox'))


# def dublicat(num):
#     l=[]
#     for i in num:
#         if i not in l:
#             l.append(i)
#     return l
# print(dublicat([1,2,3,3,3,3,4,5]))

def dublicat_ele(l):
    a=[]
    i=0
    while i<len(l):
        if l[i] not in a:
            a.append(l[i])
        i+=1
    return a
print(dublicat_ele([1,2,3,3,3,3,4,5]))


