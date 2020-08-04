class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        #initialize storage with as many Nones as capacity
        self.storage = [None] * capacity
        self.size = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.storage)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # load factor is defined as the number of items in the table divided by capacity
        return self.size / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        #high number prime shit that I need to take a cryptography class for it to make sense
        FNV_Prime = 1099511628211
        FNV_offset_basis = 14695981039346656037

        hash = FNV_offset_basis

        for char in key:
            hash = hash * FNV_Prime
            hash = hash ^ ord(char)

        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        #look onto bitwise operators
        hash = 5381

        for c in key:
            hash = (hash * 33) + ord(c)
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        #find the index in the storage list that we want
        storage_index = self.hash_index(key)

        if not self.storage[storage_index]:
            #create a new entry and put that in. Update size attr
            self.storage[storage_index] = HashTableEntry(key, value)
            self.size += 1
        #otherwise it's gonna need some space
        else:
            current_entry = self.storage[storage_index]
            #iterating through the list until you get to the end of the list or the entry with the same key
            while current_entry.next is not None and current_entry.key is not key:
                current_entry = current_entry.next
            #we looked through everyhthing and didn't find the key so just add a new thing
            if current_entry.key is key:
                current_entry.value = value
            else:
                current_entry.next = HashTableEntry(key, value)
                self.size += 1


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        #lol holy crap i worked so much harder on this than I needed to
        self.put(key,None)
        # Your code here
        # if self.get(key) is None:
        #     return "That ain't in there anywho"
        #
        # # find the index in the storage list that we want
        # storage_index = self.hash_index(key)
        # current_entry = self.storage[storage_index]
        # if current_entry.next is None:
        #     current_entry.key = None
        #     current_entry.value = None
        # else:
        #     print("anything")
        #     prev_entry = current_entry
        #     while current_entry.key is not key:
        #         prev_entry = current_entry
        #         current_entry = current_entry.next
        #         print(prev_entry, current_entry)
        #     prev_entry.next = current_entry.next
        #     current_entry.next = None
        #     current_entry.key = None
        #     current_entry.value = None



    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        #set up the index you trying to find
        storage_index = self.hash_index(key)

        #if nothings there return None
        if self.storage[storage_index] == None:
            return None
        #if the thing there is just one key-value pair, return the value
        if self.storage[storage_index].key == key:
            return self.storage[storage_index].value
        #otherwise it's a linked list that needs iterating
        else:
            #iterate through it
            current = self.storage[storage_index]
            while current.next is not None:
                current = current.next
                #and if you find the thing you're looking for then return it
                if current.key is key:
                    return current.value
            #but if you go through the whole list and it's not there
            return None


def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
