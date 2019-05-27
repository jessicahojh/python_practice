class Node(object):
    """Node in a Linked List"""

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    """Linked List"""

    def __init__(self):
        self.head = None
        self.tail = None

    def print_list(self):
        """print all items in the list"""

        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

    def find(self, data):
        """does this data exist in our list?"""

        current = self.head 

        while current is not None:
            if current.data == data:
                return True

            current = current.next

        return False

    def append(self, data):
        """append node with data to end of list"""

        new_node = Node(data)

        if self.head is None:  # if there's no head
            self.head = new_node 

        if self.tail is not None: # if there's a tail/ if list exist
            self.tail.next = new_node

        self.tail = new_node # no matter what, the new node is also a tail now

    def insert(self, data):
        """insert node with data to anywhere in the middle of the linked list"""

        pass

    def remove(self, value):
        """remove node with given value"""

        # if removing head, make 2nd item (if any) the new .head
        if self.head is not None and self.head.data == value:
            self.head = self.head.next

            if self.head is None:  # if removing the head made the list empty, 
                self.tail = None   # then tail also has to be none
            return

        # removing something other than head
        current = self.head

        while current.next is not None:

            if current.next.data == value:
                current.next = current.next.next
                if current.next is None:
                    # if removing last item, update .tail
                    self.tail = current
                return

            else:
                # haven't found yet, keep traversing
                current = current.next

    # other methods to try
    # def remove_by_index(2)
    # def insert(2, 'cardamom')

class NodeForDoubly(object):

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None


    def append(self, data):

        new_node = NodeForDoubly(data)

        if self.head is None:  # if there's no head
            new_node.prev = None
            self.head = new_node 
            self.tail = new_node

        else: 
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail.next.next = None
            self.tail = new_node


    def print_forward(self):

        current = self.head

        while current is not None:
            print(current.data)
            current = current.next


    def print_backward(self):

        current = self.tail

        while current is not None:
            print(current.data)
            current = current.prev



class NodeForCircular(object):

    def __init__(self, data):

        self.data = data
        self.next = None


class CircularLinkedList(object):

    def __init__(self):

        self.head = None

    def prepend_circular(self, data):
        
        new_node = NodeForCircular(data)

        current = self.head

        new_node.next = self.head

        if not self.head:
            new_node.next = new_node

        else:
            while current.next != self.head:
                current = current.next
            current.next = new_node

        self.head = new_node



    def append_circular(self, data):
        
        if not self.head:
            self.head = NodeForCircular(data)
            self.head.next = self.head

        else:
            new_node = NodeForCircular(data)
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def print_list_circular(self):
        
        current = self.head

        while current:
            print(current.data)
            current = current.next
            if current == self.head:
                break


if __name__ == '__main__':
    ll = LinkedList()
    ll.append("apple")
    ll.append("berry")
    ll.append("cherry")
    ll.print_list()

    print('')

    testdouble = DoublyLinkedList()
    testdouble.append("a")
    testdouble.append("b")
    testdouble.append("c")
    testdouble.append("d")
    testdouble.print_forward()
    testdouble.print_backward()

    print('')

    testcircular = CircularLinkedList()
    testcircular.append_circular(1)
    testcircular.append_circular(2)
    testcircular.append_circular(3)
    testcircular.append_circular(4)
    testcircular.print_list_circular()
    testcircular.prepend_circular(0)
    testcircular.print_list_circular()




