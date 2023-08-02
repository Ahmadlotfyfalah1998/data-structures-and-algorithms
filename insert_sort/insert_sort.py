def insert(sorted, value):
    i = 0
    while i < len(sorted) and value > sorted[i]:
        i += 1
    sorted.insert(i, value)


def insertion_sort(input):
    sorted = [input[0]]
    for i in range(1, len(input)):
        insert(sorted, input[i])
    return sorted
input_array = [5, 2, 9,0,22,99 ,44,2, 1, 3]
sorted_array = insertion_sort(input_array)
print(sorted_array) 

# i=[1,2,3]
# i.insert(1,7)
# print(i)