class Node:
    def __init__(self, value: int = None):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    ref: https://ja.wikipedia.org/wiki/%E4%BA%8C%E5%88%86%E6%8E%A2%E7%B4%A2%E6%9C%A8
    """

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, insert_value: int, node_value: Node):
        if insert_value < node_value.value:
            if node_value.left is None:
                node_value.left = Node(insert_value)
            else:
                self._insert(insert_value, node_value.left)
        elif insert_value > node_value.value:
            if node_value.right is None:
                node_value.right = Node(insert_value)
            else:
                self._insert(insert_value, node_value.right)
        else:
            print("Insert same value")

    def delete(self, value):
        if self.root is None:
            return False
        else:
            self.root = self._delete(value, self.root)

    def _delete(self, value, node_value: Node):
        if node_value is None:
            return node_value
        if value < node_value.value:
            node_value.left = self._delete(value, node_value.left)
        elif value > node_value.value:
            node_value.right = self._delete(value, node_value.right)
        else:
            if node_value.left is None:
                tmp = node_value.right
                node_value = None
                return tmp
            elif node_value.right is None:
                tmp = node_value.left
                node_value.left = None
                return tmp
            else:
                tmp = self.find_min(node_value.right)
                node_value.value = tmp.value
                node_value.right = self._delete(node_value.value, node_value.right)
        return node_value

    def find_min(self, node_value: Node):
        if self.root is None:
            return None
        while node_value.left:
            node_value = node_value.left
        return node_value

    def find(self, value):
        if self.root:
            if self._find(value, self.root):
                return True
        return False

    def _find(self, value, node_value: Node):
        if value == node_value.value:
            return True
        if value > node_value.value and node_value.right:
            return self._find(value, node_value.right)
        elif value < node_value.value and node_value.left:
            return self._find(value, node_value.left)

    def print_tree(self):
        if self.root:
            self._print_tree(self.root)

    def _print_tree(self, node_value: Node):
        if node_value:
            self._print_tree(node_value.left)
            print(node_value.value)
            self._print_tree(node_value.right)


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(2)
    bst.insert(5)
    bst.insert(6)
    bst.insert(1)
    bst.insert(8)
    bst.insert(3)
    bst.delete(6)
    bst.print_tree()
