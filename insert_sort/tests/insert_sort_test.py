import pytest
from insert_sort.insert_sort import insert,insertion_sort



def test_insert():
    actual=insertion_sort([8,4,23,42,16,15])
    expected=[4,8,15,16,23,42]
    assert actual==expected
    
def test_insert_twO():
    actual=insertion_sort([20,18,12,8,5,-2])
    expected=[-2,5,8,12,18,20]
    assert actual==expected
    
def test_insert_tree():
    actual=insertion_sort([5,12,7,5,5,7])
    expected=[5,5,5,7,7,12]
    assert actual==expected
def test_insert_four():
    actual=insertion_sort([2,3,5,7,13,11])
    expected=[2,3,5,7,11,13]
    assert actual==expected