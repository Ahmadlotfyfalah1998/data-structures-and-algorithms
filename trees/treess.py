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
              
class Tnode:
    """
    this is the tree nodes it have left and right
    """
    def __init__(self,value):
        self.value = value
        self.right=None
        self.left=None
               
class Tree:
   """
   this is tree class you can create tree with a root and left and right t node 
   and there is three methods to traverse the tree 
   1.pre_order
   2.post_order 
   3.in_order
   """
   def __init__(self):
       self.root=None
       
   def pre_order(self):
      """
      pre_order travers the tree root >> left >> right
      """
      if self.root is None:
       return None   
      else: 
       output=[]
       def _helper(root):
           output.append(root.value)
           if root.left:
               _helper(root.left)
           if root.right:
               _helper(root.right)
       _helper(self.root)
       return output
              

   def in_order(self):
    """
      in_order travers the tree left >> root >> right
    """    
    if self.root is None:
     return None   
    else:       
     output=[]   
     def _helper(root):
        
         if root.left:
             _helper(root.left)
            
         output.append(root.value)    
         if root.right:
             _helper(root.right)
     _helper(self.root)
     return output    
   def post_order(self):
       
       
    """
      post_order travers the tree left >> right >> root
    """    
    if self.root is None:
       return None   
    else:    
       output=[]
       def _helper(root):
        
          if root.left:
            _helper(root.left)
            
             
          if root.right:
            _helper(root.right)
            
          output.append(root.value) 
       _helper(self.root)      
       return output
   
   
   
   
   def max_tree(self):
      """
       this method is a method for the tree class it return the maximum 
       value in te tree 
      """
       
      if self.root is None:
           return "no max :the tree is empty"  
      else:       
       output=[]   
       def _helper(root):
        
         if root.left:
             _helper(root.left)
            
         output.append(root.value)    
         if root.right:
             _helper(root.right)
       _helper(self.root)
       
       max_tnode=output[0]
       for x in output:
           if x>max_tnode:
               max_tnode=x
       return max_tnode
              
  
       
class Binary_search(Tree):
    
    
    """
    this is binary search tree class , you can add a t node and always the smalest node will added in 
    the left and the bigger node will added in the right
    """
    def add(self, value):
        """
        this method will add a new value to the tree to the right of to the left according to its   
        """
        if self.root is None:
            self.root = Tnode(value)
        else:
            self.add_node(self.root, value)

    def add_node(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Tnode(value)
            else:
                self.add_node(current.left, value)
        else:
            if current.right is None:
                current.right = Tnode(value)
            else:
                self.add_node(current.right, value)   
    def contains(self,value):
        """
         it return true if the node in the tree and false if it not 
       
        """
        if self.pre_order()==None:
            return 'the tree is empty'
        elif value in self.pre_order():
            return True
        else:
            return False
if __name__=='__main__':
 treee = Tree()
 treee.root=Tnode('root')
 treee.root.left=Tnode('left')
 treee.root.right=Tnode('right')
 treee.root.left.left=Tnode('left,left')
 treee.root.left.right=Tnode('left,right')
 treee.root.right.left=Tnode('right,left')
 treee.root.right.right=Tnode('right,right')
 print(treee.pre_order())
 print(treee.in_order())
 print(treee.post_order())

 binary=Binary_search()
 binary.add(20)
 binary.add(2)
 binary.add(5)
 binary.add(15)
 binary.add(3)
 binary.add(2)
 binary.add(4)
 print(binary.in_order())
 print(binary.contains(3))
 print(binary.contains(7))
 print(binary.contains(2))
 print(binary.contains(10))
 print(binary.contains(300))
 print(binary.contains(8))
 
 print(binary.max_tree())