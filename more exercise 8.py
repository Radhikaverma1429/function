def max_marks(marks):
    i=0
    while i<len(marks):
        maximum=0
        j=0
        while j<len(marks[i]):
            if marks[i][j]>maximum:
                maximum=marks[i][j]
            j+=1
        i+=1
        print(maximum)
max_marks( [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]])