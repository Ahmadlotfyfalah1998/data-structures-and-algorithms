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