test1= [2,4,6,-8]
test2= [42,8,15,23,42]

def array_insert_shift(arr,n):
    arr2=[]
    mid=len(arr)//2
    for i in range(len(arr)):
     if len(arr)%2==0:
         if i==mid:
          arr2.append(n) 
          arr2.append(arr[i]) 
         else:
          arr2.append(arr[i])
     else : 
         if i-1==mid:
              arr2.append(n) 
              arr2.append(arr[i]) 
         else:
               arr2.append(arr[i])   
    return arr2        


def array_delete_shift(arr): 
    mid=len(arr)//2
    for i in range(len(arr)):    
         if i==mid:
          arr.pop(i)   
    return arr       















print( array_insert_shift(test2,16))
print( array_insert_shift(test1,5))

print(array_delete_shift(test1))
print(array_delete_shift(test2))