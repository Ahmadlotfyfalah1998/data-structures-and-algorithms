import pytest 
from stack_queue_pseudo.stack_queue_pseudo import Node,Stack,Peudo



def test_enqueue():
  queue = Peudo()
  queue.enqueue('1')
  queue.enqueue('2')
  queue.enqueue('3') 
  
  actual = queue.to_string()
  expected = "3--->>>2--->>>1--->>>"
  assert actual==expected
  
  
def test_enqueue_two():
  queue = Peudo()
  queue.enqueue('1')
  queue.enqueue('2')
  queue.enqueue('3') 
  queue.enqueue('4')
  queue.enqueue('5')
  actual = queue.to_string()
  expected = "5--->>>4--->>>3--->>>2--->>>1--->>>"
  assert actual==expected
  
  
  
  
def test_dequeue():
  queue = Peudo()
  queue.enqueue('1')
  queue.enqueue('2')
  queue.enqueue('3') 
  queue.enqueue('4')
  queue.enqueue('5')
  queue.dequeue()
  queue.dequeue()
  queue.dequeue()
  actual = queue.to_string()
  expected = "5--->>>4--->>>"
  assert actual==expected
  