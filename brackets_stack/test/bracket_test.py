import pytest 
from  brackets_stack.brackets    import    Stack,Node,validate_brackets


def test_one():
    actual=validate_brackets('{}{Code}[Fellows]([()]]]]]]])')
    expected=False
    assert actual==expected
    
def test_two():
    actual=validate_brackets('{}{Code}[Fellows]([()])')
    expected=True
    assert actual==expected
    
def test_tree():
    actual=validate_brackets('{}')
    expected=True
    assert actual==expected
def test_four():
    actual=validate_brackets('{}(){}')
    expected=True
    assert actual==expected
def test_five():
    actual=validate_brackets('()[[Extra Characters]]')
    expected=True
    assert actual==expected
def test_six():
    actual=validate_brackets('(){}[[]]')
    expected=True
    assert actual==expected
def test_seven():
    actual=validate_brackets('[({}]')
    expected=False
    assert actual==expected
def test_eight():
    actual=validate_brackets('(](')
    expected=False
    assert actual==expected
def test_nine():
    actual=validate_brackets('{(})')
    expected=False
    assert actual==expected