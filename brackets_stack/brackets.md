# Challenge Title
code challenge 13: brackets<br>

## Whiteboard Process
![Alt text](<code 13.jpg>)

## Approach & Efficiency
first we will store only brackets in the array<br>

then we will create a stack<br>

then we will loop over array and push the bracket to the stack if it opening bracket<br>

if it not we will check for the top if it same like the top like if we have } the top of stack should be { if yes it will pop from stack

and it will check if the all opening brackets equal closed brackets<br>

if the final stack is empty it will return true<br>
big O : O(n)<br>
space : O(n)<br>

## Solution 
python brackets.py<br>
test-----> pytest  <br>
