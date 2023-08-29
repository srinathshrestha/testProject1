# selection sort 
l = [5, 3, 6, 2, 10]
for i in range(len(l)):
    min = i
    for j in range(i+1, len(l)):
        if l[min] > l[j]:
            min = j
    l[i], l[min] = l[min], l[i]
print(l)