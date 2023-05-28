class   Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
        
        
class LinkedList:
    def __init__(self,head=None):
            self.head = head
            
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
            
            
    def zipLists(self,list1,list2):
     
         if list1.head is None:
            return list2.to_string()
         if list2.head is None:
            return list1.to_string()
         current1 = list1.head
         current2 = list2.head
         while current1  and current2 :
             next1 = current1.next
             next2 = current2.next
             current1.next = current2
             current2.next = next1 or next2
             current1 = next1
             current2 = next2
         return list1.to_string()
          
          
          
if __name__ =='__main__':
 list1 = LinkedList()
 list1.append(1)
 list1.append(2)
 list1.append(3)
 list2 = LinkedList()
 list2.append("a")
 list2.append("b")
 list2.append("c")

 print(list1.zipLists(list1, list2))

