l = [7, 8, 1, 2, 3, 9, 4, 5, 6, 0]


def bubble_sort(l):
    for i in range(len(l)):
        for j in range(len(l) - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


print(bubble_sort(l))
