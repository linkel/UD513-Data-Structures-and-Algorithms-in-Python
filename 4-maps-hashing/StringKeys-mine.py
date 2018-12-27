"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        # Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter 
        hash_val = ord(string[0])*100 + ord(string[1])
        if self.table[hash_val] == None:
            self.table[hash_val] = [string]
        else:
            self.table[hash_val].append(string)
        
    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        hash_val = ord(string[0])*100 + ord(string[1])
        if self.table[hash_val] != None:
            for i in self.table[hash_val]:
                if i == string:
                    return hash_val
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        hash_val = ord(string[0])*100 + ord(string[1])
        return hash_val
        
    # for myself
    def show_bucket(self, string):
        hash_val = ord(string[0])*100 + ord(string[1])
        if self.table[hash_val] != None:
            for i in self.table[hash_val]:
                print(i)
    
# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print hash_table.calculate_hash_value('UDACITY')

# Test lookup edge case
# Should be -1
print hash_table.lookup('UDACITY')

# Test store
hash_table.store('UDACITY')
# Should be 8568
print hash_table.lookup('UDACITY')

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print hash_table.lookup('UDACIOUS')
hash_table.show_bucket('UDACIOUS')