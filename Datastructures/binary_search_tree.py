class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            return

        curr = self.root
        parent = None
        while curr:
            parent = curr
            if data <= curr.data:
                curr = curr.left
            else:
                curr = curr.right
        if data <= parent.data:
            parent.left = Node(data)
        else:
            parent.right = Node(data)

    def _insert_recursive_helper(self, curr, data):
        if not curr:
            return Node(data)
        if data <= curr.data:
            curr.left = self._insert_recursive_helper(curr.left, data)
        else:
            curr.right = self._insert_recursive_helper(curr.right, data)
        return curr

    def insert_recursive(self, data):
        self.root = self._insert_recursive_helper(self.root, data)

    def search(self, data):
        if not self.root:
            return False

        curr = self.root
        while curr and data != curr.data:
            if data < curr.data:
                curr = curr.left
            else:
                curr = curr.right

        return True if curr else False

    def _search_recursive_helper(self, curr, data):
        if curr.data == data:
            return True
        if not curr:
            return False
        if data < curr.data:
            return self._search_recursive_helper(curr.left, data)
        else:
            return self._search_recursive_helper(curr.right, data)

    def search_recursive(self, data):
        return self._search_recursive_helper(self.root, data)

    def delete(self, data):
        return self._delete_helper(self.root, None, data)

    def _delete_helper(self, root, parent, data):
        if not root:
            return
        curr = root

        #we search for the node to delete
        while curr and curr.data != data:
            parent = curr
            if data < curr.data:
                curr = curr.left
            else:
                curr = curr.right

        # we can't find the node
        if not curr:
            return

        #Node is the root
        if not parent:
            self.root = None
            return

        left = True if data <= parent.data else False

        if not curr.left:
            if left:
                parent.left = curr.right
            else:
                parent.right = curr.right
        elif not curr.right:
            if left:
                parent.left = curr.left
            else:
                parent.right = curr.left
        else:
            inorder_pred = self._find_inorder_predecessor(curr.left)
            curr.data = inorder_pred
            self._delete_helper(curr.left, curr, inorder_pred)

    def delete_recursive(self, data):
        self.root = self._delete_recursive_helper(self.root, data)

    def _delete_recursive_helper(self, curr, data):
        if not curr:
            return
        if data < curr.data:
            curr.left = self._delete_recursive_helper(curr.left, data)
        elif data > curr.data:
            curr.right = self._delete_recursive_helper(curr.right, data)
        else:
            if not curr.left:
                curr = curr.right
            elif not curr.right:
                curr = curr.left
            else:
                inorder_pred = self._find_inorder_predecessor(curr.left)
                curr.data = inorder_pred
                curr.left = self._delete_recursive_helper(curr.left)
        return curr

    def _find_inorder_predecessor(self, curr):
        while curr.right:
            curr = curr.right
        return curr.data

    def _pretty_tree_helper(self, root, curr_index=0):
        if root is None:
            return [], 0, 0, 0

        line1 = []
        line2 = []
        node_repr = str(root.data)

        new_root_width = gap_size = len(node_repr)

        # Get the left and right sub-boxes, their widths, and root repr positions
        l_box, l_box_width, l_root_start, l_root_end = self._pretty_tree_helper(root.left, 2 * curr_index + 1)
        r_box, r_box_width, r_root_start, r_root_end = self._pretty_tree_helper(root.right, 2 * curr_index + 2)

        # Draw the branch connecting the current root to the left sub-box
        # Pad with whitespaces where necessary
        if l_box_width > 0:
            l_root = (l_root_start + l_root_end) // 2 + 1
            line1.append(' ' * (l_root + 1))
            line1.append('_' * (l_box_width - l_root))
            line2.append(' ' * l_root + '/')
            line2.append(' ' * (l_box_width - l_root))
            new_root_start = l_box_width + 1
            gap_size += 1
        else:
            new_root_start = 0

        # Draw the representation of the current root
        line1.append(node_repr)
        line2.append(' ' * new_root_width)

        # Draw the branch connecting the current root to the right sub-box
        # Pad with whitespaces where necessary
        if r_box_width > 0:
            r_root = (r_root_start + r_root_end) // 2
            line1.append('_' * r_root)
            line1.append(' ' * (r_box_width - r_root + 1))
            line2.append(' ' * r_root + '\\')
            line2.append(' ' * (r_box_width - r_root))
            gap_size += 1
        new_root_end = new_root_start + new_root_width - 1

        # Combine the left and right sub-boxes with the branches drawn above
        gap = ' ' * gap_size
        new_box = [''.join(line1), ''.join(line2)]
        for i in range(max(len(l_box), len(r_box))):
            l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
            r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
            new_box.append(l_line + gap + r_line)

        # Return the new box, its width and its root positions
        return new_box, len(new_box[0]), new_root_start, new_root_end

    def pretty_tree(self):
        lines = self._pretty_tree_helper(self.root, 0)[0]
        return '\n' + '\n'.join((line.rstrip() for line in lines))

    def __repr__(self):
        return self.pretty_tree()

    def __str__(self):
        return self.__repr__()


tree = BinarySearchTree()
tree.insert(8)
tree.insert(4)
tree.insert(12)
tree.insert(2)
tree.insert(6)
tree.insert(10)
tree.insert(1)
tree.insert(3)
tree.insert(5)
tree.insert(7)
tree.insert(9)
tree.insert(11)
tree.insert(13)
tree.insert(15)
tree.insert(16)
print(tree)
tree.delete(4)
print(tree)

tree2 = BinarySearchTree()
tree2.insert_recursive(8)
tree2.insert_recursive(4)
tree2.insert_recursive(12)
tree2.insert_recursive(2)
tree2.insert_recursive(6)
tree2.insert_recursive(10)
tree2.insert_recursive(1)
tree2.insert_recursive(3)
tree2.insert_recursive(5)
tree2.insert_recursive(7)
tree2.insert_recursive(9)
tree2.insert_recursive(11)
tree2.insert_recursive(13)
tree2.insert_recursive(15)
tree2.insert_recursive(16)
print(tree2)
tree2.delete(12)
print(tree2)
