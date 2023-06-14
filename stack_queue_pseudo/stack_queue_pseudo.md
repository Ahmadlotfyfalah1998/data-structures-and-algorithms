# Challenge Title
stack-queue-pseudo

## Whiteboard Process
![Alt text](code%2011.jpg)

## Approach & Efficiency
first we create two stacks<br>
for enqueue we push to the first stack<br>
for dequeue we move all nodes from first stack to  second stack<br>
then we pop the top node from the second stack<br>
 then we move the nodes from the second stack to the first stack<br>
but this time without the top element on the second<br>
stack so we delete the last element on the first stack<br>
biG O :O(n)N<br>

## Solution
 python stack_queue_pseudo.py
 test -----> pytest