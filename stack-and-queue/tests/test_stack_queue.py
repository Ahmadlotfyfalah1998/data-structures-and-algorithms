import pytest 
from stack_queue import Node,Stack,Queue

def test_stack_push():
    new_stack=Stack()
    new_stack.push(1)
    new_stack.push(2)
    new_stack.push(3)
    actual=new_stack.to_string()
    expected='{3} -> {2} -> {1} -> None'
    assert actual == expected
    
def test_stack_pop():
    new_stack=Stack()
    new_stack.push(1)
    new_stack.push(2)
    new_stack.push(3)
    new_stack.pop()
    actual=new_stack.to_string()
    expected='{2} -> {1} -> None'
    assert actual == expected
    
    
def test_stack_empty_pop():
    new_stack=Stack()
    new_stack.push(1)
    new_stack.push(2)
    new_stack.push(3)
    new_stack.pop()
    new_stack.pop()
    new_stack.pop()
    actual=new_stack.to_string()
    expected='None'
    assert actual == expected
    
    
    
def test_stack_peek():
    new_stack=Stack()
    new_stack.push(1)
    new_stack.push(2)
    new_stack.push(3)
    actual=new_stack.peek()
    
    expected=3
    assert actual == expected
def test_stack_empty():
    new_stack=Stack()
   
    actual=new_stack.to_string()
    expected='None'
    assert actual == expected
    
def test_stack_error_pop():
    new_stack=Stack()
   
   
    with pytest.raises(TypeError, match='the stack is empty'):
        new_stack.pop()
    
def test_stack_error_peek():
    new_stack=Stack()
   
   
    with pytest.raises(TypeError, match='the stack is empty'):
        new_stack.peek()
def test_queue_enqueue():
    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    actual=queue.to_string()
    expected='{1} -> {2} -> {3} -> None'
    assert actual==expected
    
def test_queue_dequeue():
    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    
    
    actual=queue.dequeue()
    expected=1
    assert actual==expected
    
def test_queue_peek():
    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    
    
    actual=queue.peek()
    expected=1
    assert actual==expected

def test_queue_multiple_dequeue():
    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    actual=queue.to_string()
    expected='None'
    assert actual==expected
    
    
def test_queue_create_empty():
    queue=Queue()
    
    actual=queue.to_string()
    expected='None'
    assert actual==expected
    
    
def test_queue_peek_error():
    queue=Queue()
    
    with pytest.raises(TypeError, match='the queue is empty'):
        queue.peek()
        
def test_queue_dequeue_error():
    queue=Queue()
    
    with pytest.raises(TypeError, match='the queue is empty'):
        queue.dequeue()