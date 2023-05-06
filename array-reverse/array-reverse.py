
test=[1,2,3,4,5,6]
test2=[89, 2354, 3546, 23, 10, -923, 823, -12]
def reverse_array (arr):  
   newArr=[]
   i= len(arr)
   while i >0:
    newArr.append(arr[i-1])
    i=i-1 
   return newArr
print(reverse_array(test))
print(reverse_array(test2))
"""
    [6, 5, 4, 3, 2, 1]
    [-12, 823, -923, 10, 23, 3546, 2354, 89]
"""
