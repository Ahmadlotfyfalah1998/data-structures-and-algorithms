class   Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
        
        
class LinkedList:
    def __init__(self,head=None):
            self.head = head
        
        
    def traverse(self):
        current=self.head
        while current:
            print(current.value)
            current=current.next
        
    def append(self,value):
        new = Node(value,None)
        if self.head is None:
            self.head = new
        else:
            current = self.head
            while current.next :
                current= current.next
            current.next = new           
        
    def insert(self,value):    
        new=Node(value)
        new.next=self.head
        self.head=new
    def to_string(self):
        current=self.head
        string=""
        if current:
         while current:
          string+=f"{{{current.value}}} -> "   
          current=current.next
        
        string+='None'  
        return string 

    def delete(self,vaalue):
        counter =0
        current=self.head
        if vaalue == 0 :
            self.head=self.head.next
        while current:
            if counter+1 == vaalue:
                
                current .next =current.next.next
            current=current.next
            counter += 1
        return print(self.to_string())
    
    def delete_element(self, element):
        
        current=self.head
        if self.head.value == element:
            self.head=self.head.next
        while current:
            if current.next :
                if current.next.value == element:
                    current.next=current.next.next
            
            if not current.next and current:
                if current.value == element:
                    current=None
            current=current.next         
        return print(self.to_string())
    
    
    def marge (self,ll1,ll2):
        cu=ll1.head
        cu2=ll2.head
        ll3=llll
        while cu or cu2:
            
            if cu and not cu2:
            elif cu2 and not cu:
            else:
                if cu.value>cu.value:
                    ll.append(cu)
                    ll.appennd(cu2)
            
                else:
                    
            cu=cu.next
            
                    
                
                
            
        
        
            
            
            
                    
          
           
        
  

if __name__ == '__main__':
   n6=Node(5)
   n5=Node(4,n6)
   n4=Node(3,n5)
   n3=Node(2,n4)
   n2=Node(1,n3)
   n1=Node(0,n2)
   
   list=LinkedList(n1)
  
   n52=Node('f')
   n42=Node('d',n52)
   n32=Node('c',n42)
   n22=Node('b',n32)
   n12=Node('a',n22)
   
   list2=LinkedList(n12)   
   
  
   list.delete_element(2)
   

   print(list.to_string())   
   