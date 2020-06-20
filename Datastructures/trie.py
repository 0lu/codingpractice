class TrieNode:
    def __init__(self, char=None):
        self.char = char
        self.children = [None] * 26
        self.is_end_word = False

    def mark_as_leaf(self):
        self.is_end_word = True

    def unmark_as_leaf(self):
        self.is_end_word = False

    def __hash__(self):
        return hash(self.char)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def get_index(self, char):
        return ord(char) - ord("a")

    def insert(self, key):
        if not key:
            return
        key = key.lower()
        curr = self.root
        for char in key:
            index = self.get_index(char)
            if not curr.children[index]:
                curr.children[index] = TrieNode(char)
                print(f"inserted node {char}")
            curr = curr.children[index]
        curr.mark_as_leaf()
        print(f"inserted word {key}")

    def search(self, key):
        if not key:
            return False
        curr = self.root
        for char in key:
            index = self.get_index(char)
            if not curr.children[index]:
                return False
            curr = curr.children[index]

        return True if curr.is_end_word else False


    def delete(self, key):
        if not self.root or not key:
            return

        self.delete_helper(self.root, key, len(key), 0)

    def has_children(self, node):
        for child in node.children:
            if child:
                return True
        return False

    def delete_helper(self, root, key, length, level):

        deleted = False

        if not root:
            return deleted

        if level == length:
            if not self.has_children(root):
                root = None
                deleted = True
            else:
                root.mark_as_leaf()
                deleted = False
        else:
            index = self.get_index(key[level])
            result = self.delete_helper(root.children[index], key, length, level + 1)

            if result:
                root.children[index] = None
                if not root.is_end_word and not self.has_children(root):
                    root = None
                    deleted = True
        return deleted


trie = Trie()
trie.insert("boy")
print(trie.search("boy"))
trie.delete("boy")
print(trie.search("boy"))
