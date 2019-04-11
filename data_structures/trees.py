class Node(object):
    """Node in a tree"""

    def __init__(self, data, children):
        self.data = data
        self.children = children

        # include parent if you can point upwards on the tree

    def __repr__(self):
        """reader-friendly representation"""

        return "<Node {data}>".format(data=self.data)

    def find_using_DFS(self, data):  # stack
        """return node object with this data."""

        to_visit = [self]

        while to_visit:
            current = to_visit.pop()

            if current.data == data:
                return current

            to_visit.extend(current.children)

 
    def find_using_BFS(self, data):  # queue
        """return node object with this data."""

        to_visit = [self]

        while to_visit:
            current = to_visit.pop(0)

            if current.data == data:
                return current

            to_visit.extend(current.children)


# You don't really need a Tree class 

# class Tree(object):
#     """tree"""

#     def __init__(self, root):
#         self.root = root

#     def __repr__(self):
#         """reader-friendly representation"""

#         return "<Tree root={root}>".format(root=self.root)

class BinarySearchNode(object):
    """binary tree node"""

    def __init__(self, data, left=None, right=None):
        self.data = data

        self.left = left
        self.right = right

    def __repr__(self):
        """reader-friendly representation"""

        return "<BinaryNode {data}>".format(data=self.data)

    def find(self, sought):
        """return node with this data"""

        current = self

        while current:

            # print("checking", current.data)

            if current.data == sought:
                return current

            elif sought < current.data:
                current = current.left

            elif sought > current.data:
                current = current.right


    def insert(self, new_data):
        """Insert new node with `new_data` to BST tree rooted here."""

        current = self

        while current:

            if current.data < new_data:
                current = current.right

            elif current.data > new_data:
                current = current.left

        if current.data < new_data:
            self.right = Node(new_data)

        else: 
            self.left = Node(new_data)

if __name__ == '__main__':
    # Create sample tree and search for nodes in it

    apple = BinarySearchNode("apple")
    ghost = BinarySearchNode("ghost")
    fence = BinarySearchNode("fence", apple, ghost)
    just = BinarySearchNode("just")
    jackal = BinarySearchNode("jackal", fence, just)
    zebra = BinarySearchNode("zebra")
    pencil = BinarySearchNode("pencil", None, zebra)
    mystic = BinarySearchNode("mystic")
    nerd = BinarySearchNode("nerd", mystic, pencil)
    money = BinarySearchNode("money", jackal, nerd)

    print("nerd = ", money.find("nerd"))     # should find
    print("banana = ", money.find("banana"))  # shouldn't find

    print("nerd = ", money.find("zebra"))     # should find

    # cobra = self.insert("cobra")

    print(money.insert("cobra"))







