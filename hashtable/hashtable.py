class HashTableEntry:
    """Linked List hash table key/value pair"""

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


# Hash Tables are essentially like dictionaries.
# Every entry has a key:value, but like a LinkedList, each entry has a next
#
# HashTables are much faster thank LinkedList b/c it's not anything like a list.
# Entries are accessed by way of a key!!
#
# Keys are like dictionaries: look up the word you want and you'll get the definition.

# DAY 3
# Caesar Ciphers
class HashTable:
    """A hash table that with `capacity` buckets
    that accepts string keys"""

    def __init__(self, capacity):
        # max number of items this HashTable can hold
        self.capacity = capacity if capacity >= MIN_CAPACITY else MIN_CAPACITY
        self.storage = [None] * capacity  # bucket to store items in
        self.items = 0  # track number of items in storage

    def get_num_slots(self):
        """Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this."""

        return self.capacity

    def get_load_factor(self):
        """Return the load factor for this hash table."""

        return self.items / self.capacity  # how quickly our hashtable will load

    def fnv1(self, key):
        """FNV-1 Hash, 64-bit

        Implement this, and DJB2."""

        fnv_offset_basis = 14695981039346656037
        fnv_prime = 1099511628211
        hash_value = fnv_offset_basis
        for byte in key:
            hash_value *= fnv_prime  # multiply hash by FNV_prime
            hash_value ^= ord(byte)  # bitwise XOR

        return hash_value

    def djb2(self, key):
        """DJB2 hash, 32-bit

        Implement this, and FNV-1."""

        hash_prime = 5381

        for byte in key:
            hash_prime = (hash_prime * 33) + ord(byte)

        return hash_prime

    def hash_index(self, key):
        """Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table."""

        # return self.fnv1(key) % self.capacity

        # this will cap out the returned value at the
        # table's capacity (hash will not be larger than capacity)
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining."""

        index = self.hash_index(key)
        self.storage[index] = HashTableEntry(index, value)
        self.items += 1

    def delete(self, key):
        """Remove the value stored with the given key.

        Print a warning if the key is not found."""

        index = self.hash_index(key)
        if not self.storage[index]:
            print("No such key exists in table")

        else:
            self.storage[index] = None
            self.items -= 1

    def get(self, key):
        """Retrieve the value stored with the given key.

        Returns None if the key is not found."""

        index = self.hash_index(key)

        return self.storage[index] if self.storage[index] else None

    def resize(self, new_capacity):
        """Changes the capacity of the hash table and
        rehashes all key/value pairs."""

        # This does not currently handle collisions, and thus would not really work
        self.capacity = new_capacity
        old_table = self.storage
        self.storage = [None] * self.capacity  # storage is new sequence of empty buckets

        for element in old_table:
            if element is not None:
                self.put(element.key, element.value)


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
