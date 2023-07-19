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







 


   def compare(self,tree2):
           arr1=self.pre_order()
           arr2=tree2.pre_order()
           counter1=0
           counter2=0
           for x in arr1:
                   if x != 'folder' :
                      counter1+=1
           for x in arr2:
                   if x != 'folder' :
                           counter2+=1
           if counter1 != counter2 :
                   return False
           else:
                   return True                                       
           

if __name__=='__main__':
  treee = Tree()
  treee.root=Tnode('folder')
  treee.root.left=Tnode('folder')
  treee.root.right=Tnode('folder')
  treee.root.left.left=Tnode('.js')
  treee.root.left.right=Tnode('.py')
  treee.root.right.left=Tnode('.py')
  treee.root.right.right=Tnode('.css')
  
#  print(treee.in_order())
#  print(treee.post_order())
  treee2 = Tree()
  treee2.root=Tnode('folder')
  treee2.root.left=Tnode('folder')
  treee2.root.right=Tnode('folder')
  treee2.root.left.left=Tnode('.js')
  
  treee2.root.right.left=Tnode('.py')
  treee2.root.right.right=Tnode('.css')
 
  print(treee.compare(treee2))
  print(treee2.pre_order())