def insertion_sort(v):
    for i in range(1, len(v)):
        x = v[i]
        j = i-1
        while j >= 0 and x < v[j]:
            v[j+1] = v[j]
            j -= 1
        v[j+1] = x

v = [25 , 48 , 37 , 12 , 57 , 86 , 33 , 92,
     25 , 48 , 37 , 12 , 57 , 86 , 33 , 92,
     25 , 48 , 37 , 12 , 57 , 86 , 33 , 92,
     25 , 48 , 37 , 12 , 57 , 86 , 33 , 92]

insertion_sort(v)
print(v)
