class PersonNode(object):
    """Node in a graph representing a person"""

    def __init__(self, name, adjacent=None):
        """create a person node with friends adjacent"""

        if adjacent is None:
            adjacent = set()

        # assert isinstance(adjacent, set), \
        #     "adjacent must be a set!"

        self.name = name
        self.adjacent = adjacent

    def __repr__(self):
        """debugging friendly representation"""

        return "<PersonNode: %s>" % self.name

class FriendGraph(object):
    """graph holding people and their friendships"""

    def __init__(self):
        """create an empty graph"""

        self.nodes = set()

    def __repr__(self):
        return "<FriendGraph: %s>" % [n.name for n in self.nodes]

    def add_person(self, person):
        """add a person to our graph"""

        self.nodes.add(person)

    def set_friends(self, person1, person2):
        """set two people as friends"""

        person1.adjacent.add(person2)
        person2.adjacent.add(person1)

    def are_connected(self, person1, person2):
        """Are two people connected? BFS"""

        possible_nodes = Queue()
        seen = set()
        possible_nodes.enqueue(person1)
        seen.add(person1)

        while not possible_nodes.is_empty():
            person = possible_nodes.dequeue()
            print("checking", person)
            if person is person2:
                return True
            else:
                for friend in person.adjacent - seen:
                    possible_nodes.enqueue(friend)
                    seen.add(friend)
                    print("added to queue:", friend)
        return False

        # recursive solution

        def are_connected_recursive(self, person1, person2, seen=None):
        """Are two people connected? DFS"""

        if not seen:
            seen = set()

        if person1 is person2:
            return True

        seen.add(person1) # keep track that we've visited here
        print("adding", person1)

        for person in person1.adjacent:

            if person not in seen:

                if self.are_connected_recursive(person, person2, seen):
                    return True

        return False









