## 0-1 Knapsack Problem

Take or leave an object with a certain value into your knapsack that has a weight limit.

### Greedy for value
Initially you might think to take objects with the highest value. But what if the objects with the highest value also weigh the most, and filling the pack with those is worse value than filling the pack with objects that are worth less but weigh the least? 

### Slow, straightforward solution:
Try every combo of objects and pick the one that's best. Brute force.

O(2^n) where n is # of objects for that solution combo. An exponential time. 

### Smarter Approach

Instead of just max value for max weight, what if we max value for min weight? 

Array to store max value for each weight up to weight limit. 

Initialize to zero. We have knapsack of weight 6. 

1 2 3 4 5 6 (max)
0 0 0 0 0 0

Here's our objects.

WEIGHT 2 5 4
VALUE  6 9 5

Update index of 2 with value 6, and everything after index 2 also with value 6. 

1 2 3 4 5 6 (max)
0 6 6 6 6 6

Next obj has more value, so replace.

1 2 3 4 5 6
0 6 6 6 9 9

Next object is weight 4, but index 4 is already a better value, so it doesn't get replaced.

Now we look at index 1, since our weight 4 obj can add to that index to make an index 5 with weight 5. But 9 is bigger than 5 so it won't replace.

Now we look at index 2, since our weight 4 can add to that index to make an index 6 with weight 11. This is better than the one in index 6! We can replace it.

1 2 3 4 5 6
0 6 6 6 9 11

Out of all these, 11 is the max. This has been solved. 

This saves a lot of time with many objects. We have precomputed max values, so we only do this work once to get those numbers. 

We iterate through objects and see if we can increase the max value of each possible weight up to our max weight. 

Runtime is O(n * W) where W is weight limit of knapsack and n is number of elements. This is a Pseudo-Polynomial Time. A true polynomial time does not have a number besides n (that is, relies only on one variable). 

This is a technique known as Dynamic Programming. 
