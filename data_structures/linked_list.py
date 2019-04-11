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

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            # did list start as empty?
            self.tail.next = new_node

        self.tail = new_node

    def remove(self, value):
        """remove node with given value"""

        # if removing head, make 2nd item (if any) the new .head
        if self.head is not None and self.head.data == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
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





