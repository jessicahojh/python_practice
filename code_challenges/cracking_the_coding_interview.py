# page 90 Array and Strings

# 1.1 Is Unique
def is_unique(string):

    dictionary = {}

    for letter in string:
        if letter in dictionary.keys():
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1

    for x in dictionary.values():
        if x == 1:
            continue
        else:
            return False

    return True

print(is_unique("beets"))
print(is_unique("qwerty"))


# 1.2 Check Permutation
def is_perm(str_1, str_2):

    if len(str_1) != len(str_2):
        return False

    dictionary_1 = {}
    dictionary_2 = {}

    for letter in str_1:
        if letter in dictionary_1.keys():
            dictionary_1[letter] += 1
        else:
            dictionary_1[letter] = 1

    for letter in str_2:
        if letter in dictionary_2.keys():
            dictionary_2[letter] += 1
        else:
            dictionary_2[letter] = 1
 

    if dictionary_1.items() == dictionary_2.items():
        return True
    else:
        return False

print(is_perm("abc", "bca"))
print(is_perm("yum", "bug"))


# 1.3 URLify
def urlify(string):
    """replace all space with '%20'"""

    answer = []

    for char in string:
        if char == " ":
            answer.append('%20')
        else:
            answer.append(char)

    return ''.join(answer)

print(urlify("hey there haha"))
print(urlify("i like python   "))


# 1.4 Palindrome Permutation

def pal_perm(string):
    """Check if the string is a permutation of a palindrome"""

    # characters need to be even numbers and only one odd

    dictionary = {}

    for char in string:
        if char in dictionary.keys():
            dictionary[char] += 1
        else:
            dictionary[char] = 1

    odd = []

    for value in dictionary.values():
        if value % 2 != 0:
            odd.append(value)

    if len(odd) > 1:
        return False
    else:
        return True


print(pal_perm("yhuhy")) #t
print(pal_perm("yhuuhy")) #t
print(pal_perm("yhuy")) #f


# 1.5 One Away

def one_edit_away(str_1, str_2):

    # one remove
    # one add
    # one replace

    pass


# 1.6 String Compression

def compress(string):

    answer = []

    current_letter = string[0]
    current_count = 0

    for char in string:
        if char != current_letter:
            answer.append(current_letter)
            current_count = str(current_count)
            answer.append(current_count)
            current_letter = char
            current_count = 1
        else:
            current_count += 1

    answer.append(current_letter)
    answer.append(str(current_count))


    return ''.join(answer)


print(compress("aabbbccc")) #a2b3c3


# 1.7 Rotate Matrix


# 1.8 Zero Matrix


# 1.9 String Rotation


# page 94 Linked Lists


class Node(object):

    def __init__(self, data):

        self.data = data
        self.next = None

class LinkedList(object):

    def __init__(self):

        self.head = None
        self.tail = None


# 2.1 Remove Duplicates
    def remove_dupe_ll(self):

        lst = []

        current = self.head 

        previous = None

        while current is not None:

            if current.data not in lst:
                lst.append(current.data)
                previous = current
                current = current.next
            elif current.data in lst:
                previous.next = current.next
                current = previous.next

    def append(self, data):
        """append node with data to end of list"""

        new_node = Node(data)

        if self.head is None:  # if there's no head
            self.head = new_node 

        if self.tail is not None: # if there's a tail/ if list exist
            self.tail.next = new_node

        self.tail = new_node

    def print_list(self):

        current = self.head

        while current is not None:
            print(current.data)
            current = current.next


# 2.2 Return Kth to last
    def return_kth_to_last(self, k):

        lst = []

        current = self.head

        while current is not None:
            lst.append(current.data)
            current = current.next

        length = len(lst)


        return lst[length-k]

# 2.3 Delete Middle Node 
    def delete_middle(self, sought):

        current = self.head

        previous = None

        while current is not None:
            if current.data != sought:
                previous = current
                current = previous.next
            elif current.data == sought:
                previous.next = current.next
                current = previous.next

# 2.4 Partition
    def partition(self, x):

        
        pass


test = LinkedList()
test.append('a')
test.append('b')
test.append('c')
test.append('b')
test.append('d')
test.append('e')

test.print_list()

test.remove_dupe_ll()
test.print_list()
print(test.return_kth_to_last(3))
test.delete_middle('b')
test.print_list()















