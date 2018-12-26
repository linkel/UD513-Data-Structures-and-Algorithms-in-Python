### Bubble Sort

Bubble Sort has time complexity of O(n^2) for worst case and average case
because it makes comparisons between two values through the entire array,
needing to make n-1 comparisons per iteration of bubbling. (n-1)(n-1) = n^2 - 2n + 1
Best case time complexity is if array is already sorted, which is O(n)
Space complexity is O(1) because it does not make a new copy of the data structure.


### Bubble Sort Quiz Answer:

[21, 4, 1, 3, 9, 20, 25, 6, 21, 14] (Original Array)
[4, 1, 3, 9, 20, 21, 6, 21, 14, 25] (1)
[1, 3, 4, 9, 20, 6, 21, 14, 21, 25] (2)
[1, 3, 4, 9, 6, 20, 14, 21, 21, 25] (3)
[1, 3, 4, 6, 9, 14, 20, 21, 21, 25] (4)

