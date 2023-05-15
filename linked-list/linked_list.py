class   Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
        
        
class LinkedList:
    def __init__(self,head=None):
            self.head = head
        
        
    def traverse(self)    :
        current=self.head
        while current:
            print(current.value)
            current=current.next
        
        
        
    def insert(self,value):    
        new=Node(value)
        new.next=self.head
        self.head=new
        
        
        
    def include(self,value):
        current=self.head
        while current:
            if current.value==value:
                return True
            current=current.next
        return False    
        
    def to_string(self):
        current=self.head
        string=""
        if current:
         while current:
          string+=f"{{{current.value}}} -> "   
          current=current.next
        
        string+='None'  
        return string   
              
        
if __name__ == '__main__':
   ahmad=Node('ahmad')
   newahmad=Node('newahmad',ahmad)
  
   list=LinkedList(newahmad)
   
   list.insert('therdahmad')
   list.traverse()
   print(list.to_string())