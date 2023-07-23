import pytest


from hashtable.hash import HashTable


def test_hash_method():
  expected = 652
  hash = HashTable()
  actual = hash._HashTable__hash('d')
  assert expected == actual
  
  
def test2_hash_method():
  expected =  879
  hash = HashTable()
  actual = hash._HashTable__hash('=')
  assert expected == actual
  
  
def test_set_method():
    ht = HashTable()
    

    ht.set('name', 'John')
    actual=ht.get('name') 
    expected = 'John' 
    assert actual==expected
    
def test2_set_method():
    ht = HashTable()
    

    ht.set('age', '20')
    actual=ht.get('age') 
    expected = '20' 
    assert actual==expected
def test5_set_method():
    ht = HashTable()
    

  
    actual=ht.get('favorites_color') 
    expected = None
    assert actual==expected
    
def test_keys():
      ht = HashTable()
    

      ht.set('name', 'John')
      ht.set('age', '20')
      ht.set('car', 'nissan')
      
      expected=['name', 'age', 'car']
      assert ht.keys()==expected
      
      
def test_collisin_keys():
      ht = HashTable()
    

      ht.set('name', 'John')
      ht.set('name', 'khalled')
      ht.set('name', 'salah')
      actual = ht.get('name')
   
      expected ='salah'
      assert actual==expected
def test2_collisin_keys():
      ht = HashTable()
    

      ht.set('name', 'John')
      ht.set('name', 'khalled')
      ht.set('name', 'salah')
      actual = ht.has('name')
   
      expected =True
      assert actual==expected


def test_collision_keys():
    ht = HashTable()

    ht.set('name', 'John')
    ht.set('name', 'khalled')
    ht.set('name', 'salah')


    values = []
    curr = ht._HashTable__buckets[ht._HashTable__hash('name')].head
    while curr:
        values.append(curr.value[1])
        curr = curr.next


    assert values == ['salah', 'khalled', 'John']