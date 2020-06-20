class TrieNode:
    def __init__(self, char=None):
        self.char = char
        self.children = {}
        self.is_end_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):
        if not key:
            return
        curr = self.root
        for letter in key:
            if letter not in curr.children:
                curr.children[letter] = TrieNode(letter)
            curr = curr.children[letter]
        curr.is_end_word = True

    def search(self, key):
        if not key:
            return
        curr = self.root
        for letter in key:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return curr.is_end_word

    def delete(self, key):
        if not key:
            return
        self.delete_helper(self.root, key, len(key), 0)

    def delete_helper(self, curr, key, length, level):
        deleted = False

        if not curr:
            return deleted

        if length == level:
            if curr.is_end_word:
                if not curr.children:
                    curr = None
                    deleted = True
                else:
                    curr.is_end_word = False
                    deleted = False
        else:
            char = key[level]
            if char in curr.children:
                result = self.delete_helper(curr.children[char], key, length, level + 1)
                if result:
                    del curr.children[char]
                    deleted = True
                    if not curr.is_end_word and not curr.children:
                        curr = None
                        deleted = True
        return deleted

trie = Trie()
trie.insert("boy")
trie.insert("girl")
trie.insert("boyer")
trie.insert("girlfriend")
print(trie.search("boy"))
trie.delete("boy")
print(trie.search("boy"))

