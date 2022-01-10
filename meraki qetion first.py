def num_function(numbers):
    i=0
    m=0
    while i<len(numbers):
        if numbers[i]>m:
            m=numbers[i]
        i+=1
    print(m)    
num_function(numbers = [3, 5, 7, 34, 2, 89, 2, 5])