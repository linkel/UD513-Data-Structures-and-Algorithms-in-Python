### DP
Break problem down to base case. Smallest computation. Like computing values for one object in the knapsack case. 

Use a lookup table that stores solutions to subproblems. In the knapsack case, we stored the weights and values in a table. 

Most DP problems are like so:
Solve problem in trivial case and collect them in that table. 

### Memoization
Memoization: storing precomputed values.

Normal computations might require repeated computations of the same thing if they are needed "on the way" to the solution through different branches of computation. Memoized computations will let you pull a previously-calculated value out of a table and use that to calculate the next piece. 