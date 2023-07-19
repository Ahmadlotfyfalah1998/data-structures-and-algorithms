import  pytest
from trees.treess import Tree, Node,Tnode,Queue,Binary_search

def test_pre_order():
   treee = Tree()
   treee.root=Tnode('root')
   treee.root.left=Tnode('left')
   treee.root.right=Tnode('right')
   treee.root.left.left=Tnode('left,left')
   treee.root.left.right=Tnode('left,right')
   treee.root.right.left=Tnode('right,left')
   treee.root.right.right=Tnode('right,right')
   actual=treee.pre_order()
   expected=['root', 'left', 'left,left', 'left,right', 'right', 'right,left', 'right,right']
   assert actual==expected
   
def test_in_order():
   treee = Tree()
   treee.root=Tnode('root')
   treee.root.left=Tnode('left')
   treee.root.right=Tnode('right')
   treee.root.left.left=Tnode('left,left')
   treee.root.left.right=Tnode('left,right')
   treee.root.right.left=Tnode('right,left')
   treee.root.right.right=Tnode('right,right')
   actual=treee.in_order()
   expected=['left,left', 'left', 'left,right', 'root', 'right,left', 'right', 'right,right']
   assert actual==expected   
   
def test_post_order():
   treee = Tree()
   treee.root=Tnode('root')
   treee.root.left=Tnode('left')
   treee.root.right=Tnode('right')
   treee.root.left.left=Tnode('left,left')
   treee.root.left.right=Tnode('left,right')
   treee.root.right.left=Tnode('right,left')
   treee.root.right.right=Tnode('right,right')
   actual=treee.post_order()
   expected=['left,left', 'left,right', 'left', 'right,left', 'right,right', 'right', 'root']
   assert actual==expected    
   
   
def test_empty_tree():
   treee = Tree()
   
   actual=treee.pre_order()
   expected=None
   assert actual==expected 
   
   
def test_one_tnode_tree():
      treee = Tree()
      treee.root=Tnode('root')
      actual=treee.pre_order()
      expected=['root']
      assert actual==expected 
      
      
def test_binary_tree():
   binary=Binary_search()
   binary.add(4)
   binary.add(2)
   binary.add(5)
   binary.add(1)
   binary.add(3)
   binary.add(7)
   binary.add(8)
   actual=binary.in_order()
   expected=[1, 2, 3, 4, 5, 7, 8]
   assert actual==expected
   
   
   
def test_contain_true():
   binary=Binary_search()
   binary.add(4)
   binary.add(2)
   binary.add(5)
   binary.add(1)
   binary.add(3)
   binary.add(7)
   binary.add(8)
   actual=binary.contains(7)
   expected=True
   assert actual==expected
   
def test_contain_false():
   binary=Binary_search()
   binary.add(4)
   binary.add(2)
   binary.add(5)
   binary.add(1)
   binary.add(3)
   binary.add(7)
   binary.add(8)
   actual=binary.contains(30)
   expected=False
   assert actual==expected
   
  ## code challenge 16 
   
def test_max_tree():
   treee = Tree()
   treee.root=Tnode(1)
   treee.root.left=Tnode(4)
   treee.root.right=Tnode(6)
   treee.root.left.left=Tnode(2)
   treee.root.left.right=Tnode(9)
   treee.root.right.left=Tnode(12)
   treee.root.right.right=Tnode(0) 
   actual=treee.max_tree()
   expected=12
   assert actual==expected
   
   
def test_max_tree_empty():
   treee = Tree()
 
   actual=treee.max_tree()
   expected="no max :the tree is empty"
   assert actual==expected