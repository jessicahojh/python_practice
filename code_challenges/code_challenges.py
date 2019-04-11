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



