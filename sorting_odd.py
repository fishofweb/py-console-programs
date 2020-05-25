def sort_array(source_array):
    
    even_={}
    
    for i in source_array:
        if i % 2 == 0:
            ind = source_array.index(i)
            even_[ind] = i
            
    arr = [i for i in source_array if i % 2 !=0]
    
    arr.sort()
    
    source_array = []
    for i in arr:
        source_array.append(i)
    for k,v in even_.items():
        source_array.insert(k, v)
    return source_array
    
y = sort_array([5, 3, 2, 8, 1, 4])
print(y)
    
    