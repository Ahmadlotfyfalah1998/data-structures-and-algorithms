# Challenge Title
Linked List Implementation
## Whiteboard Process
![Alt text](code%206%20append.jpg)
![Alt text](code%206%20insert%20before.jpg)
![Alt text](code%206%20insert%20after.jpg)



## Approach & Efficiency
#### append
the function will create a new node with parameter value<br>
the function will check the last existed next<br>
the function will insert the new node after it<br>
big O:O(n)<br>
#### insert before
the function will create a new node with parameter value<br>
the function will loop over the linked list and check for next of the current value<br>
once it find the next value equal the parameter first value it will insert the value before it<br>
it will set the next of current value equal to new node and the next of new one to the value we need to insert before it<br>
big O:O(n)<br>
#### insert after
the function will create a new node with parameter value<br>
the function will loop over the linked list and check for current value
once it find the current value equal the parameter it will set new node after it<br>
it will set the  new value as next for current value and set the next for new one the next of current
before it<br>
big O:O(n)<br>
## Solution
 python linked-list/linked_list.py
## tests
 pytest