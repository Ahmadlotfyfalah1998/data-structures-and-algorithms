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
          
          
    def to_string(self):
        current=self.top
        string=""
        if current:
         while current:
          string+=f"{{{current.value}}} -> "   
          current=current.next
        
        string+='None'  
        return string      
    
    
def validate_brackets(string):
    
    
    
        '''
        this function take a string  containing brackets and check if
        each bracket have opening and closing brackets and will return true if 
        the braket form is correct otherwise it will return false
        '''
        arr=[]
        for element in string:
            if element=='{'or  element=='}'or element=='['or  element==']'or element=='('or  element==')':
                arr.append(element)    
        stack=Stack()
        node=Node("first top")
        stack.push(node)
        boolean=True
        
        counter1=0
        counter2=0
        counter3=0
        counter4=0
        counter5=0
        counter6=0
        
        
        for element in arr:
            if element=="[" or element=='{' or element=="(": 
               
                node=Node(element)
                stack.push(node)
                continue   
            if element=="]" and stack.top.value.value=="[":
               
                    stack.pop()
                    continue        
            if  element=='}' and stack.top.value.value=="{":
                 
                    stack.pop()
                    continue

                               
            if  element==")" and  stack.top.value.value=="(":
                
                    stack.pop()
                    continue

                               
            if element==")" or element=="}" or element =="]" and stack.top.value.value== 'first top':
                boolean= False
                
                break          
        if stack.top.value.value != 'first top':
            boolean=False           
        for w in arr:
            if w =="{": 
             counter1+=1  
        for w in arr:
            if w =="}":  
             counter2+=1  
        for w in arr:
            if w =="[":  
             counter3+=1 
        for w in arr:
            if w =="]":  
             counter4+=1  
        for w in arr:
            if w =="(":  
             counter5+=1  
        for w in arr:
            if w ==")":  
             counter6+=1 
        if counter1 != counter2 or counter3 != counter4 or counter5 != counter6:
            boolean=False                 
        return boolean
             
            

        
        
        
if __name__ == "__main__":
    
    
  print(validate_brackets("{}{Code}[Fellows]([()]]]]]]])"))
  print(validate_brackets("{}{Code}[Fellows]([()])"))
  print(validate_brackets("{}"))
  print(validate_brackets("{}(){}"))
  print(validate_brackets("()[[Extra Characters]]"))
  print(validate_brackets("(){}[[]]"))
  print(validate_brackets("[({}]"))
  print(validate_brackets("(]("))
  print(validate_brackets("{(})"))