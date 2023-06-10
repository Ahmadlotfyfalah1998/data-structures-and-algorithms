class Node :
    """
    NODE CLASS
    """
    def __init__(self,value=None,next=None):
        self.value= value 
        self.next =next 
    def __str__(self):
        return f'{self.value}'    
        
class Queue:
    """
    queue class
    """
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
class Animal:
    """
    animal class , it have a name and species for each animal 
    """
    def __init__(self,name,species):
        self.name=name
        self.species=species    
    def __str__(self):
        return f'animal name is {{{self.name}}} and species is {{{self.species}}}'
     
class Animal_shelter():
    """
    shelter class it have a two queue one for cats and other one to
    dogs 
    and it have some methods like enqueue and dequeue  
    """
    def __init__(self):
        self.cat_=Queue()
        self.dog_=Queue()
         
    def enqueue(self,animal):
       """
        enqueue method , it will check for animal species and it will enqueue it to the cats queue if its 
        cat and its will enqueue it to the dogs queue if its dog  
       """
       if not isinstance(animal,Animal):
           return "plz instance"
       elif animal.species != 'cat' or animal.species != "dog":
           return "the animal should be cat or dog only"
       elif animal.species == 'cat':
           self.cat_.enqueue(Node(animal))
       elif animal.species == 'dog':
           self.dog_.enqueue(Node(animal))
            
    def dequeue(self,pref):
        """
        dequeue method , it take a pref as parameter and if the pref = dog it will dequeue from dogs queue 
        and if pref = cat it will dequeue from cats queue
        """ 
        if pref != 'cat' or pref != 'dog':
            return ' you can dequeue cat or dog only ' 
        elif pref == 'cat':
            self.cat_.dequeue()
        elif pref== 'dog':
            self.dog_.dequeue()
    def print_(self):
        # strr=''
        # current=self.cat.front
        # while current:
        #  strr+=current.value
        #  current=current.next
        # return strr
        return self.cat_.front
                
            
if __name__ == '__main__':
    catt=Animal('momo',"dog")
    shelter=Animal_shelter()
    print(shelter.enqueue(catt))
    print(shelter.print_())
    