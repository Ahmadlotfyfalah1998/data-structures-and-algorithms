import pytest 
from tree_intersection.trees import tree_intersection,Tree,Tnode

def test_one_tree():
 treee = Tree()
 treee.root=Tnode('8')
 treee.root.left=Tnode('3')
 treee.root.right=Tnode('10')
 treee.root.left.left=Tnode('1')
 treee.root.left.right=Tnode('14')
 treee.root.right.left=Tnode('1')
 treee.root.right.right=Tnode('7')

 treee2 = Tree()
 treee2.root=Tnode('5')
 treee2.root.left=Tnode('33')
 treee2.root.right=Tnode('0')
 treee2.root.left.left=Tnode('8')
 treee2.root.left.right=Tnode('10')
 treee2.root.right.left=Tnode('99')
 treee2.root.right.right=Tnode('88')
 actual=tree_intersection(treee,treee2)
 expected=['8', '10']
 assert actual==expected    
 
def test_two_tree():
 treee = Tree()
 treee.root=Tnode('99')
 treee.root.left=Tnode('3')
 treee.root.right=Tnode('10')
 treee.root.left.left=Tnode('33')
 treee.root.left.right=Tnode('14')
 treee.root.right.left=Tnode('1')
 treee.root.right.right=Tnode('7')

 treee2 = Tree()
 treee2.root=Tnode('5')
 treee2.root.left=Tnode('33')
 treee2.root.right=Tnode('0')
 treee2.root.left.left=Tnode('8')
 treee2.root.left.right=Tnode('10')
 treee2.root.right.left=Tnode('99')
 treee2.root.right.right=Tnode('88')
 actual=tree_intersection(treee,treee2)
 expected=['33', '10', '99']
 assert actual==expected    
 
def test_none_tree():
 treee = Tree()
 treee.root=Tnode('8')
 treee.root.left=Tnode('3')
 treee.root.right=Tnode('10')
 treee.root.left.left=Tnode('1')
 treee.root.left.right=Tnode('14')
 treee.root.right.left=Tnode('1')
 treee.root.right.right=Tnode('7')

 treee2 = Tree()
 treee2.root=Tnode('11')
 treee2.root.left=Tnode('111')
 treee2.root.right=Tnode('111')
 treee2.root.left.left=Tnode('11111')
 treee2.root.left.right=Tnode('111111')
 treee2.root.right.left=Tnode('22')
 treee2.root.right.right=Tnode('222')
 actual=tree_intersection(treee,treee2)
 expected=[]
 assert actual==expected    