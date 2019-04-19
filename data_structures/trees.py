class Node(object):
    """Node in a tree"""

    def __init__(self, data, children=None):
        self.data = data
        self.children = children or []

        # include parent if you can point upwards on the tree

    def __repr__(self):
        """reader-friendly representation"""

        return "<Node {data}>".format(data=self.data)

    def add_to_tree(self, data, new_data):
        """Add node with new data to tree using DFS"""

        to_visit = [self] # assume not empty and no dupe

        while to_visit:
            current = to_visit.pop()

            if current.data == data:
                current.children.append(Node(new_data))

            to_visit.extend(current.children)

# Advantages:

# Depth-first search on a binary tree generally requires less memory than breadth
# -first.
# Depth-first search can be easily implemented with recursion.
# Disadvantages

# A DFS doesn't necessarily find the shortest path to a node, while breadth-first 
# search does.


    def find_using_DFS(self, data):  # stack
        """return node object with this data."""

        to_visit = [self]

        while to_visit:
            current = to_visit.pop()

            if current.data == data:
                return current

            to_visit.extend(current.children)

# Advantages:

# A BFS will find the shortest path between the starting point and any other 
# reachable node. A depth-first search will not necessarily find the shortest path.
# Disadvantages

# A BFS on a binary tree generally requires more memory than a DFS.

 
    def find_using_BFS(self, data):  # queue
        """return node object with this data."""

        to_visit = [self]

        while to_visit:
            current = to_visit.pop(0)

            if current.data == data:
                return current

            to_visit.extend(current.children)

# When to use one over the other?


# You don't really need a Tree class 

# class Tree(object):
#     """tree"""

#     def __init__(self, root):
#         self.root = root

#     def __repr__(self):
#         """reader-friendly representation"""

#         return "<Tree root={root}>".format(root=self.root)

class BinaryTreeNode(object):
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

            print("checking", current.data)

            if current.data == sought:
                return current

            elif sought < current.data:
                current = current.left

            elif sought > current.data:
                current = current.right


    def insert(self, new_data):
        """Insert new node with `new_data` to BST tree rooted here."""

        current = self # assume not empty and no dupe

        prev_head = None
        # to keep track of where the last head was

        while current:
            prev_head = current
            if new_data < current.data: 
                current = current.left
                # print(current.data)

            elif new_data > current.data: 
                current = current.right
                # print(current.data)

        if new_data < prev_head.data:
            prev_head.left = BinaryTreeNode(new_data)

        elif new_data > prev_head.data:
            prev_head.right = BinaryTreeNode(new_data)


    def print_tree_in_order(self):

        current = self

        if current.left:
            current.left.print_tree_in_order()

        print(current)

        if current.right:
            current.right.print_tree_in_order()


if __name__ == '__main__':
    # Create sample tree and search for nodes in it

    # apple = BinaryTreeNode("apple")
    # ghost = BinaryTreeNode("ghost")
    # fence = BinaryTreeNode("fence", apple, ghost)
    # just = BinaryTreeNode("just")
    # jackal = BinaryTreeNode("jackal", fence, just)
    # zebra = BinaryTreeNode("zebra")
    # pencil = BinaryTreeNode("pencil", None, zebra)
    # mystic = BinaryTreeNode("mystic")
    # nerd = BinaryTreeNode("nerd", mystic, pencil)
    # money = BinaryTreeNode("money", jackal, nerd)

    # print("nerd = ", money.find("nerd"))     # should find
    # print("banana = ", money.find("banana"))  # shouldn't find

    # print("nerd = ", money.find("zebra"))     # should find

    # cobra = self.insert("cobra")


    food = Node('food', [Node('mexican'), Node('chinese'), Node('japanese')])
    # mexican = Node('mexican', ['burritos', 'salsa', 'tacos'])
    # chinese = Node('chinese', ['noodles', 'rice', 'dim sum'])
    # japanese = Node('japanese', ['ramen', 'sushi', 'curry'])
    food.add_to_tree('mexican', 'burritos')

    print(food.find_using_BFS('burritos'))
    print('^look here')





    # [10, 4, 20, 6, 25, 1]
    tree = BinaryTreeNode(10)
    tree.insert(4)
    tree.insert(20)
    tree.insert(6)
    tree.insert(25)
    tree.insert(1)

    print(tree.find(25))
    print('')

    tree.print_tree_in_order()











