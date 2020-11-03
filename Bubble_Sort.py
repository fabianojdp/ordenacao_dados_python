def bubble_sort(v):
    for i in range(len(v)-1):
        for j in range(len(v)-i-1):
            if(v[j] > v[j+1]):
                v[j], v[j+1] = v[j+1], v[j]

v = [25 , 48 , 37 , 12 , 57 , 86 , 33 , 92,
     25 , 48 , 37 , 12 , 57 , 86 , 33 , 92,
     25 , 48 , 37 , 12 , 57 , 86 , 33 , 92,     
     25 , 48 , 37 , 12 , 57 , 86 , 33 , 92]

bubble_sort(v)
print(v)
