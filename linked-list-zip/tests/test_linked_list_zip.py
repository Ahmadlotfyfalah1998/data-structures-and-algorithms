import pytest
from linked_list_zip import LinkedList,Node

def test_zip_lists():
    list1 = LinkedList()
    list1.append(1)
    list1.append(2)
    list1.append(3)
    list2 = LinkedList()
    list2.append(4)
    list2.append(5)
    list2.append(6)
    actual = list1.zipLists(list1, list2)
    expected = "{1} -> {4} -> {2} -> {5} -> {3} -> {6} -> None"
    assert actual == expected

def test_zip_lists_two():
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(2)
    list2 = LinkedList()
    list2.append(6)
    list2.append(7)
    actual = list1.zipLists(list1, list2)
    expected = "{1} -> {6} -> {3} -> {7} -> {2} -> None"
    assert actual == expected

def test_zip_lists_three():
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list2 = LinkedList()
    list2.append(5)
    list2.append(6)
    list2.append(4)
    actual = list1.zipLists(list1, list2)
    expected = "{1} -> {5} -> {3} -> {6} -> {4} -> None"
    assert actual == expected



def test_zip_lists_empty_one():
    list1 = LinkedList()
    list1.append(1)
    list1.append(2)
    list1.append(3)
    list2 = LinkedList()
   
    actual = list1.zipLists(list1, list2)
    expected = "{1} -> {2} -> {3} -> None"
    assert actual == expected








