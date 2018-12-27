### Hash Functions

Using a hash function, we can perform lookups in constant time. This contrasts with the use of lists and sets, which take linear time for lookups. 

The way it works is that we have a value that we pass through some function to get a hash value, and use the hash value as a location in the array we store to. That way we can immediately know where a value is stored since we know the hash value. 

For example, if we had numbers as values, we could take the remainder of that number when divided by another number, and use the remainder as the location in an array. 

Ex:

4979 as our number, and 109 as the hash function division. 4979 % 109 is 74, so we store that number in our array[74] position. 

### Collisions

What if we have two numbers that end up at the same position when we run them through our hash function? 

1. We can change our hash and make it bigger, so that each colliding value gets its own location in the array.

The downsides with the above approach are that this increases the space complexity, and if this is being performed reactively, then changing the hash function, recalculating, and copying the old values into a new array also increases some time complexity.

2. Instead of storing one value in each array location, we can make a "bucket" of values by creating a list in each array location. 

The downsides with this approach are that searching through each bucket now takes linear time complexity according to the size of each bucket. In the worst case, if all values end up stored in the same bucket, we now have O(n) time like we did with a list. 

Other methods include perhaps making a second hash function in each bucket to further divide up the elements. 

### Load Factor

Load factor is the # of entries divided by the # of buckets. 

### Quiz Answer:

Coworker has a hash function that divides a group of values by 100 and uses remainder as key. Values are 100 numbers, all divisible by 5. 

What is the load factor? 

It is 1, because there are 100 numbers, and the hash function has 100 unique spots. 

What number would you recommend his function to divide by to speed it up?

87
107 <---- 
125
1001

87 creates collisions. 
125 is divisible by 5 and hence also creates collisions. 
1001 is wasted space.

### Hash Maps and String Keys

Starting with a key value pair, one can run the keys through a hash function and then store the value in the bucket belonging to the hashed result of the key. 

This can be done with strings too, most typically by using the ASCII value of the string. Python's ord() function converts a char into its ASCII value, and the chr() function converts it back.

Apparently the standard in Java prefers big hash tables over collisions, so they use an equation like:
s[0]*31^(n-1) + s[1]*31^(n-2) + ... s[n-1]