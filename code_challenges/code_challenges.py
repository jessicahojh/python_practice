# Determine if a number is "happy"
# Input: 19
# Output: true
# Explanation: 
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

def is_happy(number):

    # if number == 1:
    #     return True

    # else:
    #     number = list(number)
    #     for num in number:

    pass



# Show indexes of even numbers
# [1, 2, 3, 4, 6, 8] ----> [1, 3, 4, 5]

def show_even(lst):

    answer = []
    index = 0 

    for num in lst:
        if num % 2 == 0:
            answer.append(index)
            index = index + 1
        else:
            index = index + 1

    return answer

print(show_even([1, 2, 3, 4, 6, 8]))

# convert snake case to camel case
# 'hello_there' ----> helloThere

def convert_to_camel(string):

    answer = []

    string = string.split("_")
    print(string)

    answer.append(string[0])

    for word in string[1:]:
        word = word.title()
        answer.append(word)


    return ''.join(answer)

print(convert_to_camel("hello_there"))

# find the mode. the mode is the most reoccurring item

def find_mode(lst):

    dictionary = {}

    for num in lst:
        dictionary[num] = dictionary.get(num, 0) + 1

    highest_count = max(dictionary.values())

    mode = set()

    for num, count in dictionary.items():
        if count == highest_count:
            mode.add(num)

    return mode


print(find_mode([1, 2, 2, 2, 3]))  # {2}
print(find_mode([3]))              # {3}
print(find_mode([1, 1, 2, 2]))     # {1, 2}



# find the range of a given list of numbers

def find_range(lst):

    smallest = [lst[0]]
    biggest = [lst[0]]

    for num in lst[1:]:
        if num < smallest[0]:
            del smallest[0]
            smallest.append(num)

    for num in lst[1:]:
        if num > biggest[0]:
            del biggest[0]
            biggest.append(num)

    answer = (smallest, biggest)
    return(answer)


print(find_range([3, 4, 2, 5, 10]))  # (2, 10)
print(find_range([43, 3, 44, 20, 2, 1, 100])) # (1, 100)
print(find_range([7])) # (7, 7)

# return True if any two nums in a list sum to 0

def sum_to_zero(lst):


    for num in lst:

        if -num in lst:
            return True
    else:
        return False


print(sum_to_zero([1, 2, 3])) #F
print(sum_to_zero([1, 2, -2])) #T
print(sum_to_zero([1])) #F


# is the word a anagram of a palindrome


# pseudocode
# if length is 1, return true
# create dictionary and create letter, count for key, values
# if values have more than one "1" return False

def is_anagram_of_pal(word):

    if len(word) == 1:
        return True

    dictionary = {}

    for letter in word:
        dictionary[letter] = dictionary.get(letter, 0) + 1

    count = dictionary.values()  

    ones = 0

    for num in count:
        if num == 1:
            ones = ones + 1

    if ones <= 1:
        return True
    return False


print(is_anagram_of_pal('abb')) #T
print(is_anagram_of_pal('c')) #T
print(is_anagram_of_pal('asdfdsa')) #T
print(is_anagram_of_pal('qwerrewq')) #T
print(is_anagram_of_pal('abbi')) #F
print(is_anagram_of_pal('abie')) #F


def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses."""

    num_guesses = 0

    higher_than = 0
    lower_than = 101
    guess = None

    while guess != val:
        num_guesses += 1
        guess = (lower_than - higher_than) // 2 + higher_than

        if val > guess:
            higher_than = guess

        elif val < guess:
            lower_than = guess

    return num_guesses

print(binary_search(75))
print(binary_search(10))
print(binary_search(88))
print(binary_search(52))
print(binary_search(100))


# Given two lists. concatenate them (that is, combine them into a single list).

def cat_list(lst1, lst2):

    new_list = []

    for num in lst1:
        new_list.append(num)

    for num in lst2:
        new_list.append(num)

    return new_list


print(cat_list([1, 2], [3, 4]))


# Given a string with a month and a year (separated by a space), return the number 
# of days in that month.

# Leap years are a bit tricky. A year is a leap year if and only if:

# it is evenly divisible by 4
# except if it is divisible by 100, in which case it isn’t
# except if it is divisible by 400, in which case it is
# So, for example, 1904 was a leap year. 1900 is divisible by 100, so it wasn’t. 
# 2000 is divisible by 400, so it was.

def two_sum(lst, target):

    indexes = []

    for i, num in enumerate(lst):
        if target - num in lst:
            indexes.append(i)
            first_num = num
            break

    second_num = target - first_num

    for i, num in enumerate(lst):
        if second_num == num:
            indexes.append(i)
            break

    return indexes



print(two_sum([2, 7, 11, 15], 9))




def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses."""

    assert 0 < val < 51, "Val must be between 1-100"

    num_guesses = 0

    higher_than = 0
    lower_than = 51
    guess = None

    while guess != val:
        num_guesses += 1
        guess = (lower_than - higher_than) // 2 + higher_than

        if val > guess:
            higher_than = guess

        elif val < guess:
            lower_than = guess

    # END SOLUTION

    return num_guesses

print(binary_search(10))

class Node:
    """Binary search tree node."""

    def __init__(self, data, left=None, right=None):
        """Create node, with data and optional left/right."""

        self.left = left
        self.right = right
        self.data = data

    def is_valid(self):
        """Is this tree a valid BST?"""

        def _ok(n, lt, gt):
            """Check this node & recurse to children

                lt: left children must be <= this
                gt: right child must be >= this
            """

            if n is None:
                # base case: this isn't a node
                return True

            if lt is not None and n.data > lt:
                # base case: bigger than allowed
                #  we'll fail fast here
                return False

            if gt is not None and n.data < gt:
                # base case: smaller than allowed
                #  we'll fail fast here
                return False

            if not _ok(n.left, n.data, gt):
                # general case: check our left child
                #   all descendants of left child must be
                #   less than our data (and greater than
                #   whatever we had to be greater than).
                #   if not, fail fast.
                return False

            if not _ok(n.right, lt, n.data):
                # general case: check our right child
                #   all descendants of right child must be
                #   greater than our data (and less than
                #   whatever we had to be less than)
                #   if not, fail fast.
                return False

            # If we reach here, we're either a leaf node with
            # valid data for lt/gt, or we're higher up, but
            # our recursive calls downward succeeded. Either way,
            # this is our winning base case.
            return True

        # Call our recursive function, starting here.
        # Since we haven't yet gone left or right, we don't know
        # our `lt` or `gt` values yet, so pass None for these.

        return _ok(self, None, None)


def polish_calc(s):

    tokens = s.split()
    print(tokens)

    operand2 = int(tokens.pop())
    print(operand2)

    while tokens:
        # Grab the right-most number
        operand1 = int(tokens.pop())
        print(operand1)

        # Grab the right-most operand
        operator = tokens.pop()
        print(operator)

        # Do the math and use the result as our "right-hand" value
        # for the next time we do math

        if operator == "+":
            operand2 = operand1 + operand2
            print(operand2)

        elif operator == "-":
            operand2 = operand1 - operand2
            print(operand2)

        elif operator == "*":
            operand2 = operand1 * operand2
            print(operand2)

        elif operator == "/":
            operand2 = operand1 // operand2
            print(operand2)

    # The final result is the result of the most recent operation

    return operand2


# print(polish_calc("- 1 2")) # 1 - 2 = -1
print(polish_calc("- 9 * 2 3")) # 9 - (2 * 3) = 3
# print(polish_calc("/ 6 - 4 2")) # 6 / (4 - 2) = 3


# Jason Question 1

def switch_vowels(string):

    vowels = 'aeiou'
    make_lst = []

    for letter in string:
        make_lst.append(letter)

    i = 0
    j = len(string) - 1

    while i < j:

        if make_lst[i] not in vowels:
            i = i + 1
            continue

        if make_lst[j] not in vowels:
            j = j - 1
            continue

        # if make_lst[i] in vowels and make_lst[j] in vowels:
        make_lst[i], make_lst[j] = make_lst[j], make_lst[i]
        i = i + 1
        j = j - 1

    return ''.join(make_lst)

print(switch_vowels("aebvio")) #oibvea
print(switch_vowels("dqaebvop")) #dqoebvap
print(switch_vowels("iqaebvop")) #oqeabvip
print('')


# Jason Question 2

# from collections import defaultdict


def find_all_anagrams_in_book(book):

    words = book.split(' ')
    make_list = []

    for word in words:
        make_list.append(word)

    dictionary = {}

    for w in make_list: 

        if ''.join(sorted(w)) in dictionary:
            dictionary[''.join(sorted(w))].append(w) 
        else:
            dictionary[''.join(sorted(w))] = [w]

    for x in dictionary.values():
        if len(x) > 1:
            print(x)

print(find_all_anagrams_in_book('the cat act all these bear bare in those who tac'))

def sort_two_arrays(a, b):

  a = sorted(a)
  b = sorted(b)

  answer = []

  i = 0
  j = 0


  while len(a) != 0 and len(b) != 0: 

    if a[0] <= b[0]:
      answer.append(a[0])
      del(a[0])
      # i = i + 1
    elif a[0] > b[0]:
      answer.append(b[0])
      del(b[0])
      # j = j + 1

  if len(a) == 0:
    answer.extend(b)

  else:
    answer.extend(a)


  return answer


print(sort_two_arrays([15, 12, 14, 14, 9, 2, 2, 7, 6, 19],[14, 16, 12, 7, 15, 4, 6, 16, 7, 5]))


# Result: [2, 2, 4, 5, 6, 6, 7, 7, 7, 9, 12, 12, 14, 14, 14, 15, 15, 16, 16, 19]




def rev_string_recursively(string):

    if len(string) == 1:
        return string



    return string[-1:] + rev_string_recursively(string[:-1])



print(rev_string_recursively('balloon')) #noollab
#n+balloo
#no+ballo
#noo+ball
#nool+bal
#nooll+ba
#noolla+b  now returns that



def sum_range(n):

    if n == 1:
        return 1

    return sum_range(n-1) + n




print(sum_range(3)) # 1+2+3 = 6
print(sum_range(5)) # 1+2+3+4+5 = 15




def factorial(n):

    if n == 1:
        return 1


    return factorial(n-1) * n


print(factorial(3)) #1*2*3 = 6
print(factorial(5)) #1*2*3*4*5 = 120


def warm_temp(lst):

    answer = []

    i = 0
    
    while i != len(lst)-1:

        if lst[i] > max(lst[i+1:]):
            answer.append(0)
            i = i + 1

        else:

            j = i + 1
            if lst[j] > lst[i]:
                answer.append(j-i)
                i = i + 1
            
            elif lst[j] < lst[i]:
                while lst[j] < lst[i]:
                    j = j + 1
                answer.append(j-i)
                i = i + 1
                

    answer.append(0)

    return answer

print(warm_temp([73, 74, 75, 71, 69, 72, 76, 73])) #[1, 1, 4, 2, 1, 1, 0, 0]


# def jump_game(lst):

#     i = 0

#     while i != len(lst)-1:
#         i = i + lst[i]

#     if i == len(lst)-1:
#         return True
#     else:
#         return False



# print(jump_game([2,3,1,1,4])) #true
# print(jump_game([3,2,1,0,4])) #false


# practice trees

class Tree(object):

    def __init__(self, data, children=None):

        self.data = data
        self.children = children or []

    def add_to_tree(self, data, new_data):

        to_visit = [self]

        while to_visit:

            current = to_visit.pop()

            if current.data == data:
                current.children.append(Tree(new_data)) 
            to_visit.extend(current.children)

    def find_using_DFS(self, sought):

        to_visit = [self]

        while to_visit:

            current = to_visit.pop()

            if current.data == sought:
                return("We found it!")
            to_visit.extend(current.children)

        return("We couldn't find it")


    def find_using_BFS(self, sought):
        
        to_visit = [self]

        while to_visit:

            current = to_visit.pop(0)

            if current.data == sought:
                return("We found it!")
            to_visit.extend(current.children)

        return("We couldn't find it")

test_tree = Tree("people", [])
test_tree.add_to_tree("people", "TK")
test_tree.add_to_tree("people", "Jessica")
test_tree.add_to_tree("Jessica", "Jennifer")

print(test_tree.find_using_DFS("Jennifer"))
print(test_tree.find_using_BFS("Matthew"))


# Practice Binary tree class

class BinaryTree(object):

    def __init__(self, data, left=None, right=None):

        self.data = data
        self.left = left
        self.right = right

    def add_to_binary_tree(self, new_data):

        current = self

        new_node = BinaryTree(new_data)

        while current:

            previous_head = current

            if new_data < current.data:
                current = current.left

            elif new_data > current.data:
                current = current.right


        if new_data < previous_head.data:
            previous_head.left = new_node
        elif new_data > previous_head.data:
            previous_head.right = new_node



    def find(self, data):

        current = self

        while current:

            if data == current.data:
                return("We found it!")

            elif data < current.data:
                current = current.left

            elif data > current.data:
                current = current.right 

        return("We couldn't find it")



test_binary_tree = BinaryTree(4)
test_binary_tree.add_to_binary_tree(6)
test_binary_tree.add_to_binary_tree(2)
test_binary_tree.add_to_binary_tree(10)
test_binary_tree.add_to_binary_tree(8)
test_binary_tree.add_to_binary_tree(0)
test_binary_tree.add_to_binary_tree(3)

print(test_binary_tree.find(10))
print(test_binary_tree.find(22))


            
# set

a = set()

a.add(1)
a.add(2)
a.add(5)
a.add(1)

print(a)



# tuple

b = (1, 2)
print(b)

c = (1,2,3,4,5,6)

# c[1] = 4 #can't do this


print(c)


"""
Convert numeric string to number withoutusing python's built in functions.
"""


def str2int(num_str):

    dec_places = {6:100000, 5:10000, 4:1000, 3:100, 2:10, 1:1}
    char_digit = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5,  '6':6, '7':7, '8':8, '9':9}

    iter = len(num_str)

    number = 0

    for char in num_str:
        number += (char_digit[char] * dec_places[iter])
        iter -= 1

    return number

print(str2int('623297'))


# practice bubble sort

def bubble_sort(lst):

    for i in range(0, len(lst)-1):

        made_swap = False

        for j in range(0, len(lst) - 1 - i):

            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                made_swap = True

        if not made_swap:
            break

    return lst

print(bubble_sort([2,5,10,22,1,4]))



































