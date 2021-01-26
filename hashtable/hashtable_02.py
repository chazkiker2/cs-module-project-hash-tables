class HashTableEntry:
    """Linked List hash table key/value pair"""

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


MIN_CAPACITY = 8
FNV_offset_basis_64 = 5381
FNV_prime_64 = 33


class HashTable:
    """A hash table that with `capacity` buckets
    that accepts string keys"""

    def __init__(self, capacity):
        self.capacity = capacity if capacity >= MIN_CAPACITY else MIN_CAPACITY
        self.storage = [None] * capacity  # bucket to store items in
        self.item_count = 0  # track number of item_count in storage

    def get_num_slots(self):
        """Return the length of the list you're using to hold the hash
        table data. (Not the number of item_count stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this."""

        return self.capacity

    def get_load_factor(self):
        """Return the load factor for this hash table."""

        return self.item_count / self.capacity  # how quickly our hashtable will load

    @staticmethod
    def fnv1(key):
        """FNV-1 Hash, 64-bit"""

        fnv_prime = 1099511628211
        fnv_offset = 14695981039346656037
        for byte in key:
            fnv_offset *= fnv_prime  # multiply hash by FNV_prime
            fnv_offset ^= ord(byte)  # bitwise XOR

        return fnv_offset

    @staticmethod
    def djb2(key):
        """DJB2 hash, 32-bit"""

        str_key = str(key).encode()
        hash_ = FNV_offset_basis_64

        for byte in str_key:
            hash_ *= FNV_prime_64
            hash_ ^= byte
            hash_ &= 0xffffffffffffffff  # 64-bit hash

        return hash_
        # hash_prime = 5381
        # for byte in key:
        #     hash_prime = (hash_prime * 33) + ord(byte)
        #
        # return hash_prime

    def hash_index(self, key) -> int:
        """Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table."""

        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining."""

        index = self.hash_index(key)

        current_entry = self.storage[index]

        while current_entry is not None and current_entry.key != key:
            current_entry = current_entry.next

        if current_entry is not None:
            current_entry.value = value

        else:
            new_entry = HashTableEntry(key, value)
            new_entry.next = self.storage[index]
            self.storage[index] = new_entry

            self.item_count += 1

            if self.get_load_factor() > 0.7:
                self.resize(self.capacity * 2)

    def delete(self, key):
        """Remove the value stored with the given key.

        Print a warning if the key is not found."""

        index = self.hash_index(key)
        if not self.storage[index]:
            print("No such key exists in table")

        else:
            self.storage[index] = None
            self.item_count -= 1

    def get(self, key):
        """Retrieve the value stored with the given key.

        Returns None if the key is not found."""

        index = self.hash_index(key)
        # if self.storage[index]:
        #     return self.storage[index].value
        # else:

        return self.storage[index].value if self.storage[index] is not None else None

    def resize(self, new_capacity):
        """Changes the capacity of the hash table and
        rehashes all key/value pairs."""

        # This does not currently handle collisions, and thus would not really work
        old_storage = self.storage
        self.capacity = new_capacity
        self.storage = [None] * self.capacity  # storage is new sequence of empty buckets
        old_item_count = self.item_count

        for bucket_item in old_storage:
            current_entry = bucket_item
            if current_entry is not None:
                self.put(current_entry.key, current_entry.value)
                current_entry = current_entry.next

        self.item_count = old_item_count


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
