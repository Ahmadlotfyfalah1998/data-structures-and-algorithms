# class Node :
#     def __init__(self,value=None,next=None):
#         self.value= value 
#         self.next =next 
# class Stack:
#     def __init__(self,top=None):
#        self.top = top 
         
         
#     def push(self,value):
#       node=Node(value)
#       if self.top is None:
#           self.top=node   
#       else:    
#         node.next=self.top
#         self.top=node 
        
#     def pop(self):
#          if self.top is None:
#              raise TypeError ('the stack is empty')
#          else:       
#              node = self.top
#              self.top=node.next
#              node.next=None
             
#              return node.value
         
         
#     def peek (self):
#          if self.top is None:
#              raise TypeError('the stack is empty')
#          else:       
#              return self.top.value
    
    
#     def is_empty (self):
#           if self.top is None:
#              return True
#           else:       
#              return False
         
#     def __str__(self):
#         current=self.top
#         while current:
#           print (current.value)
#           current = current.next
          
          
#     def to_string(self):
#         current=self.top
#         string=""
#         if current:
#          while current:
#           string+=f"{{{current.value}}} -> "   
#           current=current.next
        
#         string+='None'  
#         return string       
            
            
            
#     def getMax(self):
#         biggest=self.top
#         current=self.top
#         while current:
#           if current.value >  biggest.value:
#               biggest=current
#           current=current.next   
#         return biggest.value
    
    
    
    
# if __name__=='__main__':
#  first=Stack()
#  first.push(9)
#  first.push(100)
#  first.push(60)
#  first.push(8)
#  first.push(3)
#  print( first.to_string())
#  print(first.getMax())
# x='asdfdgh'
# arr=[]
# for o in x  :
#  arr.append(o)
 
# print(arr)
def validate_brackets( string):
        arr=[]
        for x in string:
            if x=='{'or  x=='}'or x=='['or  x==']'or x=='('or  x==')':
                arr.append(x)
        return arr
    
print(validate_brackets('qwr(jt[g])-}--{{{{}}}'))