def list_1(string_list):
    i=0
    str1=string_list
    empty=[]
    while i<len(string_list):
        if string_list[i] not in str1:
            empty.append(string_list[i])
        i=i+1
list_1(string_list = ["Delhi", "Delhi", "Mumbai", "Mumbai", "Delhi", "Chennai", 'Chennai']) 