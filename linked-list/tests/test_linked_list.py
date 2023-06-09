import pytest

from linked_list import LinkedList,Node

def test_empty_linked_list():
    new_list = LinkedList()
    actual = new_list.head
    expected = None
    assert actual == expected
     
def test_insert_node():
    new_list = LinkedList()
    new_list.insert(1)
    actual = new_list.head.value
    expected = 1
    assert actual == expected
    
def test_head():
    new_list = LinkedList()
    new_list.insert("first is a head")
    actual = new_list.head.value
    expected = "first is a head"
    assert actual == expected
    
def test_insert_multiple_nodes():
    new_list = LinkedList()
    new_list.insert("first")
    new_list.insert("second")
    new_list.insert("third")
    actual = new_list.head.value
    expected = "third"
    actual2=new_list.head.next.value
    expected2 = "second"
    assert actual == expected
    assert actual2 == expected2
    
def test_include():
       new_list = LinkedList()
       new_list.insert("first")
       new_list.insert("second")
       new_list.insert("third")
       
       actual = new_list.include("first")
       expected= True
       assert actual == expected
       actual = new_list.include("four")
       expected= False
       assert actual == expected
       
def test_existed_values():
     new_list = LinkedList()
     new_list.insert("first")
     new_list.insert("second")
     new_list.insert("third")
     actual=new_list.to_string()
     excepted="{third} -> {second} -> {first} -> None"
     assert excepted==actual
     
def test_append():
    new_list = LinkedList()
    new_list.append("first")
    new_list.append("second")
    new_list.append("third")

    actual=new_list.to_string()
    excepted="{first} -> {second} -> {third} -> None"
    assert excepted==actual
      
      
def test_insert_before():
    new_list = LinkedList()
    new_list.append("first")
    new_list.append("second")
    new_list.append("third")
    new_list.Insert_Before("second","beforeSec")
    actual=new_list.to_string()
    expected="{first} -> {beforeSec} -> {second} -> {third} -> None"
    assert expected==actual
    
    
def test_insert_before_first():
    new_list = LinkedList()
    new_list.append("first")
    new_list.append("second")
    new_list.append("third")
    new_list.Insert_Before("first","beforefirst")
    actual=new_list.to_string()
    expected="{beforefirst} -> {first} -> {second} -> {third} -> None"
    assert expected==actual
    
    
def test_insert_after():
    new_list = LinkedList()
    new_list.append("first")
    new_list.append("second")
    new_list.append("third")
    new_list.insert_after("second","afterSecound")
    actual=new_list.to_string() 
    expected="{first} -> {second} -> {afterSecound} -> {third} -> None"
    assert expected==actual
    
def test_insert_after_last():
    new_list = LinkedList()
    new_list.append("first")
    new_list.append("second")
    new_list.append("third")
    new_list.insert_after("third","afterthird")
    actual=new_list.to_string()
    expected="{first} -> {second} -> {third} -> {afterthird} -> None"
    assert expected==actual


def test_kth_lastone():
    new_list = LinkedList()
    new_list.append("first")
    new_list.append("second")
    new_list.append("third")
    actual=new_list.linked_list_kth(0)
    expected="third"
    assert expected==actual
    
def test_kth():
    new_list = LinkedList()
    new_list.append("first")
    new_list.append("second")
    new_list.append("third")
    actual=new_list.linked_list_kth(1)
    expected="second"
    assert expected==actual
    
def test_kth_head():
    new_list = LinkedList()
    new_list.append("first")
    new_list.append("second")
    new_list.append("third")
    actual=new_list.linked_list_kth(2)
    expected="first"
    assert expected==actual   
    

def test_kth_grater():
    new_list = LinkedList()
    new_list.append("first")
    new_list.append("second")
    new_list.append("third")

    with pytest.raises(TypeError, match='this number is larger than the linked list length'):
        new_list.linked_list_kth(7)
        
def test_kth_same():
    new_list = LinkedList()
    new_list.append("first")
    new_list.append("second")
    new_list.append("third")

    with pytest.raises(TypeError, match='this number is larger than the linked list length'):
        new_list.linked_list_kth(3)
        
def test_kth_nigative():
    new_list = LinkedList()
    new_list.append("first")
    new_list.append("second")
    new_list.append("third")

    with pytest.raises(TypeError, match='Negative value not accepted'):
        new_list.linked_list_kth(-3)
        
        
        
def test_kth_one_element():
    new_list = LinkedList()
    new_list.append("first")
    
    actual=new_list.linked_list_kth(0)
    expected="first"
    assert expected==actual