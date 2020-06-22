
class NoSuchKeyException(Exception):
    pass

class EntryNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self):
        self.size = 10
        self.capacity = 0
        self.hashtable = [None] * self.size
        self.load_factor = 0.6

    def __insert(self, hashtable, key, value):
        position = self.get_position(key)
        if not hashtable[position]:
            hashtable[position] = EntryNode(key, value)
            return

        curr = hashtable[position]
        while curr and curr.next:
            if curr.key == key:
                curr.value = value
                return
            curr = curr.next

        curr.next = EntryNode(key, value)

    def insert(self, key, value):
        position = self.get_position(key)
        if not self.hashtable[position]:
            self.hashtable[position] = EntryNode(key, value)
            self.capacity += 1
            return

        curr = self.hashtable[position]
        if curr.key == key:
            curr.value = value
            return

        while curr and curr.next:
            if curr.key == key:
                curr.value = value
                return
            curr = curr.next

        curr.next = EntryNode(key, value)
        self.capacity += 1

        if (self.capacity / self.size) > self.load_factor:
            self.resize()

    def delete(self, key):
        position = self.get_position(key)

        if not self.hashtable[position]:
            raise NoSuchKeyException(f"{key} does not exist in hashtable")

        if self.hashtable[position].key == key:
            self.hashtable[position] = self.hashtable[position].next
            self.capacity -= 1
            return

        curr = self.hashtable[position]
        prev = None
        while curr and curr.key != key:
            prev = curr
            curr = curr.next

        prev.next = curr.next
        self.capacity -= 1

    def find(self, key):
        position = self.get_position(key)
        if not self.hashtable[position]:
            return None

        curr = self.hashtable[position]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next

        return None

    def resize(self):
        new_size = self.size * 2
        new_hastable = [None] * new_size

        for i in range(len(self.hashtable)):
            if not self.hashtable[i]:
                continue
            curr = self.hashtable[i]
            while curr:
                self.__insert(new_hastable, curr.key, curr.value)
                curr = curr.next

        self.hashtable = new_hastable
        self.size = new_size

    def get_position(self, key):
        return hash(key) % self.size

ht = HashTable()
ht.insert("boy", 1)
ht.insert("girl", 2)
ht.insert("niece", 3)
ht.insert("good", 4)
ht.insert("bad", 8)
ht.insert("boy", 10)
ht.insert("bake", 1)
ht.insert("simpson", 2)
ht.insert("tall", 3)
ht.insert("God", 4)
ht.insert("Jesus", 8)
ht.insert("Grace", 10)
ht.delete("boy")
print(ht.find("boy"))