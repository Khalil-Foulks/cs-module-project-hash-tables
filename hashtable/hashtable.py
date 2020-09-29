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

class LinkedList:
    def __init__(self):
        self.head = None

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        # self.capacity = capacity
        # # creating a hash table containing a slot of None, the length of capaciity
        # self.table = [None] * self.capacity

        # ---------LINKED LIST IMPLEMENTATION-------------------
        self.capacity = capacity
        # creating a hash table containing a slot of empty Linked Lists, the length of capaciity
        self.table = [LinkedList()] * self.capacity
        self.item_count = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len([None] * self.capacity)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here

        return self.item_count / len(self.table)


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        #Psuedocode
        """
        algorithm fnv-1 is
            hash := FNV_offset_basis do

            for each byte_of_data to be hashed
                hash := hash × FNV_prime
                hash := hash XOR byte_of_data

            return hash 
        """

        # Your code here
        fnv_offset_basis = 14695981039346656037
        fnv_prime = 1099511628211

        hash = fnv_offset_basis

        for bytes in key:
            hash = hash * fnv_prime
            # XOR is '^'; ord() function returns the number representing the unicode code of a specified character.
            hash = hash ^ ord(bytes)
        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """

        
        #Psuedocode in c
        """
        unsigned long
        hash(unsigned char *str)
        {
            unsigned long hash = 5381;
            int c;

            while (c = *str++)
                hash = ((hash << 5) + hash) + c; /* hash * 33 + c */

            return hash;
        }
        """
        # Your code here

        hash = 5381

        for bytes in key:
            hash = ((hash << 5) + hash) + ord(bytes)
        return hash
        


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # # calculate index for key; store as index
        # index = self.hash_index(key)

        # # update the value in the table at the index with new key,value pair
        # self.table[index] = HashTableEntry(key,value)

        # ---------LINKED LIST IMPLEMENTATION-------------------
        # calculate index for key; store as index
        index = self.hash_index(key)
        # create node(HashTableEntry)
        node = HashTableEntry(key,value)
        
        # check if the linked list at that index for the key
        # if LL is empty 
        if self.get(key) is None:
            # insert node at head of linked list at table index
            self.table[index].head = node
            # increase count by 1
            self.item_count += 1

        # if the key is found, overwrite the value stored there
        else:
            cur = self.table[index].head
            # while cur is not pointing to None, search for the key
            while cur.next:
                # if cur key matches input key
                if cur.key == key:
                    # overwrite the value stored there input value
                    cur.value = value
                # otherwise traverse linked list
                cur = cur.next

            # otherwise update node.next to be current head
            node.next = cur
            # current head becomes the inserted node
            cur = node



    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # # Your code here
        # # store the hash_index as index
        # index = self.hash_index(key)

        # # check to see if key is not None at index
        # if self.table[index]:
        #     # restore the key's value as None
        #     self.put(key, None)
        # else:
        #     return print("key not found")  

    # ---------LINKED LIST IMPLEMENTATION-------------------   
        # store the hash_index as index
        index = self.hash_index(key)

        # check to see if key is not None at index 
        if self.get(key):
            # check if the list is empty
            if self.head is None:
                return None
            
            # Deleting from head
            if self.head.key == key:
                # store current head node as old_head
                old_head = self.head
                # move head pointer to next node
                self.head = self.head.next
                # old head's next pointer should point to None
                old_head.next = None
                # return deleted Node
                return old_head

            # Deleting from anywhere that's not the head
            # create prev pointer
            prev = self.head
            # create current node pointer
            cur = self.head.next
            while cur is not None: 
                if cur.key == key:
                    # prev next pointer becomes cur.next node
                    prev.next = cur.next
                    # cur.next now  points to None
                    cur.next = None
                    # return cur node
                    return cur
                # otherwise prev pointer moves down list
                prev = prev.next
                # cur pointer moves down list
                cur = cur.next
            # If we get here, we didn't find it
            return None
        else:
            return print("key not found")

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # # calculate index for key; store as index
        # index = self.hash_index(key)

        # # store key/value table entry at index
        # table_entry = self.table[index]
        # # return table entries value
        # return table_entry.value
    
    # ---------LINKED LIST IMPLEMENTATION-------------------
        # calculate index for key; store as index
        index = self.hash_index(key)

        # store linkedlist at table index as linkedlist
        linkedlist = self.table[index]

        # create a pointer for current node
        cur = linkedlist.head

        # check if head is None
        if cur is None:
            return None
         

        # while current node is not None
        while cur is not None:
            # check if current node key matches value
            if cur.key == key:
                # if so return current
                return cur.value
            # otherwise move pointer to next node  
            cur = cur.next
        # return none if key is not in list
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
