# def check(list1,list2):
#     i=0
#     empty=[]
#     while i<len(list1):
#         if list1[i] in list2:
#             empty.append(list1[i])
#         i+=1 
#     return empty
# a=check(list1 = [1, 342, 75, 23, 98] ,list2 = [75, 23, 98, 12, 78, 10, 1]) 
# print(a)


list1 = [75, 23, 98, 12, 78, 10, 1]
list2 = [1, 342, 75, 23, 98]
i=0
empty=[]
while i<len(list1):
    if list1[i] in list2:
        empty.append(list1[i])
    i+=1
print(empty)

