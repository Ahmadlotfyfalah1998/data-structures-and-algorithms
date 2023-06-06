class Node :

   
    
    def __init__(self,value=None,next=None):
        self.value= value 
        self.next =next 
        
    def __str__(self):
        return f'{self.value}'
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
          
          
         
       
class Peudo:
    
    
    '''
    this class is for two stack do a queue behaviour
    '''
    def __init__(self):
        self.first=Stack()
        self.second=Stack()
        
        
        
         
    def enqueue(self,value):
        '''
        enqueue method like queue
        '''
        self.first.push(value)
        
        
        
    def dequeue(self):
        '''
        dequeue method like queue
        '''
        if self.first.top is  None:
            raise TypeError ('the queue is empty')
        else:
            
           temp=self.first.top
           
           
           while temp :
               
               self.first.top = temp.next
               self.second.push(temp)
               
               temp=temp.next
           
           self.second.pop() 
           
             
           temp=self.second.top
           
           while temp:
               self.second.top=temp.next
               self.first.push(temp)
          
               temp=temp.next
           temp=self.first.top    
       
       
       
    def to_string(self):
        current=self.first.top
        sstr=''
        while current:
          sstr+= f'{current.value}--->>>' 
          current=current.next
        return sstr  
if __name__=='__main__':
    
 queue = Peudo()
 queue.enqueue('1')
 queue.enqueue('2')
 queue.enqueue('3') 

 queue.enqueue('4')
 queue.enqueue('5')
 print( queue.to_string())
 
#  queue.enqueue('6')
#  queue.print_()

#  queue.dequeue()
#  queue.print_()
#  queue.dequeue()
 

 

