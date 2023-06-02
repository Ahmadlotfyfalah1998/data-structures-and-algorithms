class Node :
    def __init__(self,value=None,next=None):
        self.value= value 
        self.next =next 
class Stack:
    def __init__(self,top=None):
       self.top = top 
         
         
    def push(self,value):
      node=Node(value)
      if self.top is None:
          self.top=node   
      else:    
        node.next=self.top
        self.top=node 
    def pop(self):
         if self.top is None:
             raise TypeError ('the stack is empty')
         else:       
             node = self.top
             self.top=node.next
             node.next=None
             
             return node.value
         
         
    def peek (self):
         if self.top is None:
             raise TypeError('the stack is empty')
         else:       
             return self.top.value
    
    
    def is_empty (self):
          if self.top is None:
             return True
          else:       
             return False
         
    def __str__(self):
        current=self.top
        while current:
          print (current.value)
          current = current.next
          
          
    def to_string(self):
        current=self.top
        string=""
        if current:
         while current:
          string+=f"{{{current.value}}} -> "   
          current=current.next
        
        string+='None'  
        return string       
          
class Queue:
    def __init__(self):
        self.front = None
        self.back = None 
        
    def enqueue(self,value):
        node=Node(value)
        if self.front is  None:
            self.front = node
            self.back = self.front
   
        
        else:
            self.back.next=node
            self.back=node
            
    def dequeue(self):
     if self.front is  None: 
        raise TypeError('the queue is empty')
     else:
        node=self.front
        self.front=self.front.next
        node.next=None 
        return node.value 
      
    def is_empty(self):
        if self.front:
            return False
        else:
            return True 
    def peek(self):
        if self.front is None:
          raise TypeError("the queue is empty")
        else:
          return self.front.value
     
    def __str__(self):
        current=self.front
        while current:
         print(current.value) 
         current=current.next     
         
    def to_string(self):
        current=self.front
        string=""
        if current:
         while current:
          string+=f"{{{current.value}}} -> "   
          current=current.next
        
        string+='None'  
        return string       
              
         
if __name__=='__main__':
 first=Stack()
 first.push(1)
 first.push(2)
 first.push(3)
 first.push(4)
 first.push(5)

#  print(first.pop())
#  print(first.peek())
#  print(first.is_empty())
 print( first.to_string())
#  first.__str__()
 q=Queue()
 q.enqueue(1)
 q.enqueue(2)
 q.enqueue(3)
 q.enqueue(4)
 q.enqueue(5)
#  q.dequeue()
#  print(q.peek())
#  print(q.is_empty())
#  q.__str__()
 print( q.to_string())