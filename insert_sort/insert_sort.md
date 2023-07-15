# algorithm
### insertion_sort


1. Create an empty array called sorted. This array will store the sorted elements.
2. Set the first element of sorted as the first element of the input array. This is done to initialize the sorted array with at least one element.
3. Iterate through each element in the input array starting from the second element (index 1):
a. Call the insert function, passing the sorted array and the current element from the input array.
4. Return the sorted array, which now contains all the elements sorted in ascending order.


### insert 
1. Initialize a variable i to 0. This variable will keep track of the index where the value should be inserted.
2. While i is less than the length of the sorted array (and) value is greater than the element at sorted[i]:
Increment i by 1. This moves the index i forward until either reaching the end of the sorted array or finding an element greater than value.
3. Insert the value at index i in the sorted array. This is done using the insert method, which shifts existing elements to the right to make space for the value at the desired index.
 # traceing 

insertion_sort([5, 2, 4, 6, 1, 3]) Initial State: input = [5, 2, 4, 6, 1, 3], sorted = [5] <br>

Iteration 1: Inserting 2 into sorted. Intermediate sorted state: [2, 5]<br>

Iteration 2: Inserting 4 into sorted. Intermediate sorted state: [2, 4, 5]<br>

Iteration 3: Inserting 6 into sorted. Intermediate sorted state: [2, 4, 5, 6]<br>

Iteration 4: Inserting 1 into sorted. Intermediate sorted state: [1, 2, 4, 5, 6]<br>

Iteration 5: Inserting 3 into sorted. Intermediate sorted state: [1, 2, 3, 4, 5, 6]<br>

Final sorted state: [1, 2, 3, 4, 5, 6]<br>



## big numbers O : O(n^2)
## space complexity O(n)


