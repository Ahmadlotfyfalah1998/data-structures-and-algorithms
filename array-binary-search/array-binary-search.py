# test1=[2,4,6,8,10,12]
# test2=[3,6,9,12,15,18,21]
# test3=[50,55,60,65,70]
# test4=[-3,7,-11,4,6,-1]   
# def find_value_index(arr, val):
#     index = -1
#     for i in range(len(arr)):
#         if arr[i] == val:
#             index = i
#             break
#     return index 
# print(find_value_index(test1,8))  # 3
# print(find_value_index(test2,11)) #-1
# print(find_value_index(test3,60)) # 2
# print(find_value_index(test4,-2)) #-1
# print(find_value_index(test4,6))  # 4
r=[[1,2,3],[3,2,100]]
def find_value_index(arr):
    arr2=[]
    for x in arr:
     c=0
     n=0
     while n < len(x):
         c+= x[n]
         n=n+1
     arr2.append(c)    
        
    return arr2     
           
print(find_value_index(r))
                    