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
    
      
    def append(self,value):
        new = Node(value,None)
        if self.head is None:
            self.head = new
        else:
            current = self.head
            while current.next :
                current= current.next
            current.next = new   


    def Insert_Before(self,beforeit,new):
        new_node=Node(new)
        current= self.head
        if self.head.value == beforeit:
          
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while current.next :
            if current.next.value == beforeit:
               
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
      
        

        
    def insert_after(self,afterit,new):
        new_node=Node(new)
        current= self.head
        while current:
            if current.value == afterit:
                new_node.next=current.next
                current.next=  new_node
                
                return
            current = current.next   
        
    def linked_list_kth(self, value):
        if value >=0:
             current=self.head
             len=0
             while current:
              len+=1
              current=current.next
             if value >= len:
               raise TypeError("this number is larger than the linked list length")
             else:
               index=len-value-1
               counter=0
               newcurrent=self.head
               while counter<index:
                   counter+=1
                   newcurrent=newcurrent.next
               return newcurrent.value
        else:
            raise TypeError("Negative value not accepted")            
                 
    def reverse(self,ll):
        current=ll.head
        newlist=[]
        revered_list=[]
        while current:
         newlist.append(current.value)   
         current=current.next
        length=len(newlist) 
        while length>0:
            revered_list.append(newlist[length-1])
            length=length-1
        if newlist==revered_list:
         return True
        else :
         return False
        
if __name__ == '__main__':
   ahmad=Node('15')
   newahmad=Node('1',ahmad)
  
   list=LinkedList(newahmad)
   
   list.insert('3')

   list.append("3")
   list.Insert_Before("1","15")
   
   print(list.to_string())   
   print(list.reverse(list))
#    print(list.linked_list_kth(7))
   
   
   
   
   
   
   
   
   
   
   
   

   