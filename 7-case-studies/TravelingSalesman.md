## TSP

Optimization problem. What's the fastest way for our salesman to get home given a graph? 

Apparently this is used in microchip design and DNA sequencing. 

## Category: NP-Hard

NP-Hard means known algorithm in polynomial time. That is, things like O(n^2), O(n), O(2). 

## Two algo solution types

Exact, which will be in pseudo polynomial time.

Approximate, which will find a near-optimal solution in a quicker time (some of which are actually polynomial time!).

### Exact Algo

- Brute Force: Takes factorial time. O(n!)
- Dynamic Programming: 
    - Held-Karp Algorithm: O(n^2 * 2^n)

### Approximation Algo

- Christofides Algorithm: turns the graph into a tree, starting node is a root, and traverses through it in a way such that it guarantees that the result it finds is at most 50% longer than the shortest route. 

- There exist some slight improvements on this algo, but the Christofides one is the main one. 
