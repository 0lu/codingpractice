from collections import defaultdict


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, key):
        if not key:
            return
        curr = self.root
        for letter in key:
            if letter not in curr:
                curr[letter] = {}
            curr = curr[letter]
        curr["*"] = {}

    def search(self, key):
        if not key:
            return
        curr = self.root
        for letter in key:
            if letter not in curr:
                return False
            curr = curr[letter]
        return True if "*" in curr else False

    def delete_helper(self, curr, key, length, level):
        deleted = False
        if not curr:
            return deleted

        if length == level:
            if curr == {}:
                deleted = True
            else:
                if "*" in curr:
                    del curr["*"]
                    deleted = False
        else:
            child_result = self.delete_helper(curr.get(key[level]), key, length, level + 1)
            if child_result:
                curr[key[level]] = {}
                if curr == {}:
                    deleted = True
                else:
                    deleted = False
            else:
                deleted = False

        return deleted

    def delete(self, key):
        if not key:
            return
        self.delete_helper(self.root, key, len(key), 0)


trie = Trie()
trie.insert("boy")
trie.insert("girl")
trie.insert("boyer")
trie.insert("girlfriend")
print(trie.search("boy"))
print(trie.search("girlfri"))
trie.delete("boy")
print(trie.search("boy"))

