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


class Double_Node(object):

    def __init__(self, data):

        self.data = data
        self.next = None
        self.prev = None

class Double_LinkedList(object):

    def __init__(self):

        self.head = None
        self.tail = None

    def double_append(self, data):
        """append node with data to end of list"""

        new_node = Double_Node(data)

        if self.head is None:  # if there's no head
            self.head = new_node 

        if self.tail is not None: # if there's a tail/ if list exist
            self.tail.next = new_node
            self.prev = self.tail

        self.tail = new_node

    def double_print_list(self):

        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

    def double_print_backwards(self):

        current = self.tail

        while current is not None:
            print(current.data)
            current = current.prev

# 2.5 Sum Lists

    # def sum_rev_list(self, x, y):

    #     current_1 = self.tail
    #     current_2 = 

    #     while current is not None:

    # pass


# 2.6 Palindrome

    def is_palindrome(self):

        count = 0

        current = self.head

        while current is not None:
            count += 1
            current = current.next

        c = 0

        current_head = self.head
        current_tail = self.tail

        while c < count/2:
          
            if current_head.data == current_tail.data:
                print(current_head.data, current_tail.data)
                current_head = current_head.next
                current_tail = current_tail.prev
                c += 1
            else:
                return False

        return True

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
print('')

# ll_1 = Double_LinkedList()
# ll_1.double_append(7)
# ll_1.double_append(1)
# ll_1.double_append(6)

# ll_2 = Double_LinkedList()
# ll_2.double_append(5)
# ll_2.double_append(9)
# ll_2.double_append(2)

# ll_1.double_print_list()
# ll_2.double_print_list()

check_pal_1 = Double_LinkedList()
check_pal_1.double_append(1)
check_pal_1.double_append(2)
check_pal_1.double_append(3)
check_pal_1.double_append(2)
check_pal_1.double_append(1)

check_pal_2 = Double_LinkedList()
check_pal_2.double_append(1)
check_pal_2.double_append(2)
check_pal_2.double_append(3)
check_pal_2.double_append(3)
check_pal_2.double_append(2)
check_pal_2.double_append(1)

check_pal_3 = Double_LinkedList()
check_pal_3.double_append(1)
check_pal_3.double_append(2)
check_pal_3.double_append(3)
check_pal_3.double_append(4)
check_pal_3.double_append(5)
check_pal_3.double_append(6)

check_pal_4 = Double_LinkedList()
check_pal_4.double_append(1)
check_pal_4.double_append(2)
check_pal_4.double_append(3)
check_pal_4.double_append(4)
check_pal_4.double_append(5)

# print(check_pal_1.is_palindrome())
# print(check_pal_2.is_palindrome())
# print(check_pal_3.is_palindrome())
# print(check_pal_4.is_palindrome())

check_pal_4.double_print_backwards()




# Moderate page 181

# 16.1 Number Swapper (swap in place)

def num_swapper(lst, num_1, num_2):

    for index1, num1 in enumerate(lst):
        if num1 == num_1:
            save_num1 = num_1
            
    for index2, num2 in enumerate(lst):
        if num2 == num_2:
            lst[index2] = save_num1
            lst[index1] = num2

    return lst

print('')
print(num_swapper([2, 7, 8, 1, 6], 8, 6)) #[2, 7, 6, 1, 8]
print('')



def living_people(lst):

    """find the year with the most living people"""

    dictionary = {}

    for pairs in lst:
        a, b = pairs
        while a <= b:
            if a in dictionary.keys():
                dictionary[a] += 1
            elif a not in dictionary.keys():
                dictionary[a] = 1
            a += 1

    most = max(dictionary.values())

    for year, count in dictionary.items():
        if count == most:
            return year

print(living_people([(1994, 2000), (1999, 2002), (1998, 1999)])) #1999


# def english_integer(number):

#     number = str(number)

#     number_in_list = []

#     for n in number:
#         number_in_list.append(n)

#     answer = []

#     while number_in_list:
#         number_in_list.pop()


#     print(number_in_list)


# print(english_integer(1234)) #one thousand two hundred thirty four


def count_2s(n):
    """count the number of 2's that appear from 0-n"""

    count = 0

    for num in range(n+1):
        num = str(num)
        for n in num:
            if n == "2":
                count = count + 1

    return count


print(count_2s(25)) #9







