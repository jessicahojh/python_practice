# 1. Two Sum
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

# 2. Reverse Integer 
def rev_int(number):


    lst = []

    for num in str(number):
        lst.append(num)

    if number > 0:
        return ''.join(lst[::-1])

    else:
        lst = lst[1:]
        return("-"+''.join(lst[::-1]))


print(rev_int(123))
print(rev_int(-123))
print(rev_int(120))

# 3. Roman to Integer
def rom_int(roman):

    num = 0 
    precal = 0

    dictionary = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

    for i in range(len(roman)-1,-1,-1): # iterating backwards
        val = dictionary[roman[i]] # get the value from the key

        if precal > val:
            num -= dictionary[roman[i]]
        else:
            num += dictionary[roman[i]]
                
        precal = val
        
    return num


print(rom_int("III")) #3
print(rom_int("IV")) #4
print(rom_int("IX")) #9
print(rom_int("LVIII")) #58
print(rom_int("MCMXCIV")) #1994

# 4. Longest Common Prefix
def prefix(lst):

    if not lst:
            return ""
            
    for i, letter_group in enumerate(zip(*lst)):
        if len(set(letter_group)) > 1:
            return lst[0][:i]
    else:
        return min(lst)

print(prefix(["flower","flow","flight"])) # "fl"
print(prefix(["dog","racecar","car"]))   # ""

# 5. 3Sum
def three_sum(nums):
    """Find all unique triplets in the array which gives the sum of zero."""

    res = []

    nums.sort() #[-4, -1, -1, 0, 1, 2]

    for i in range(len(nums)-2): #range(4)
        if i > 0 and nums[i] == nums[i-1]:
            continue

        l, r = i+1, len(nums)-1

        while l < r:
            s = nums[i] + nums[l] + nums[r]

            if s < 0:
                l +=1 

            elif s > 0:
                r -= 1

            else:
                res.append((nums[i], nums[l], nums[r]))

                while l < r and nums[l] == nums[l+1]:
                    l += 1

                while l < r and nums[r] == nums[r-1]:
                    r -= 1

                l += 1; r -= 1
    return res


print(three_sum([-1, 0, 1, 2, -1, -4])) #[-1, 0, 1] and [-1, -1, 2]
print(three_sum([-5, 2, 3, 7, -10]))

# 6. 3Sum Closest

def threeSumClosest(num, target): #O(n^2)

        num.sort()
        result = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):
            j, k = i+1, len(num) - 1
            while j < k:
                sum = num[i] + num[j] + num[k]
                if sum == target:
                    return sum
                
                if abs(sum - target) < abs(result - target):
                    result = sum
                
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
            
        return result

print(threeSumClosest([-1, 2, 1, -4], 1)) #2

def threeSumClosest(nums, target):
    nums.sort()
    res = sum(nums[:3])
    for i in range(len(nums)):
        l, r = i+1, len(nums)-1
        while l < r:
            s = sum((nums[i], nums[l], nums[r]))
            if abs(s-target) < abs(res-target):
                res = s
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else: # break early 
                return res
    return res

print(threeSumClosest([-1, 2, 1, -4], 1)) #2

# 7 Letter Combinations of a Phone Number

def phone_map(number):

    dictionary = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'],
    '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'],
    '8':['t','u','v'], '9':['w','x','y','z']}

    made_to_lst = []

    for num in number:
        made_to_lst.append(num)


    first_nums_letters = dictionary[made_to_lst[0]]
    second_num_letters = dictionary[made_to_lst[1]]

    holder = ''
    all_combos = []

    i = 0
    length = len(second_num_letters)

    for letter in first_nums_letters:
        while i < length:
            holder = letter + second_num_letters[i]
            i += 1
            all_combos.append(holder)
        i = 0

    return all_combos

print(phone_map('23'))
print(phone_map('79'))

# 8. 4Sum

def fourSum(nums, target):

        nums.sort()
        ans = []

        for a in range(len(nums)-3):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            for b in range(a+1,len(nums)-2):
                if b > a+1 and nums[b] == nums[b-1]:
                    continue
                c, d = b+1, len(nums)-1
                while c < d:
                    tot = nums[a]+nums[b]+nums[c]+nums[d]
                    if tot == target:
                        ans.append([nums[a],nums[b],nums[c],nums[d]])
                    if tot <= target:
                        c += 1
                        while nums[c] == nums[c-1] and c < d:
                            c += 1
                    if tot >= target:
                        d -= 1
                        while nums[d] == nums[d+1] and c < d:
                            d -= 1
        return ans

print(fourSum([1, 0, -1, 0, -2, 2], 0)) # [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]


# 9. Remove Nth Node From End of List

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#     def removeNthFromEnd(self, head, n):
#         curr=head
#         prev=None
#         temp=head
#         for i in range(n):
#             temp=temp.next
#         cand=temp==None
#         while not cand:
#             temp=temp.next
#             cand=temp==None
#             prev=curr
#             curr=curr.next
#         if curr==head:
#             head=head.next
#         else:
#             prev.next=curr.next
#         return head

# print(removeNthFromEnd(2))

# 10. Valid Parentheses

def is_valid(string): # only using one type

    holder = []

    open_brac = ['(']
    close_brac = [')']

    for brac in string:
        if len(holder) == 0 and brac in close_brac:
            return False
        elif brac in open_brac:
            holder.append(brac)
        elif len(holder) > 0 and brac in close_brac:
            holder.pop()


    if len(holder) == 0:
        return True
    return False

print(is_valid('((()))'))
print(is_valid('(())('))
print(is_valid(')'))
print('')


def is_valid(s): # using all three brac types

    holder = []

    open_brac = '([{'
    close_brac = ')]}'

   
    for item in s:
        if item in open_brac:
            holder.append(item)
        else:
            if not holder or open_brac.find(holder.pop()) != close_brac.find(item):
                return False
    return not holder


print(is_valid("()"))
print(is_valid("()[]{}"))
print(is_valid("([)]"))
print(is_valid("{[]}"))
print('')

def test(string): # This works too!

    holder = []

    open_brac = '([{'
    close_brac = ')]}'

    for brac in string:
        if len(holder) == 0 and brac in close_brac:
            return False
        elif brac in open_brac:
            holder.append(brac)
        elif len(holder) > 0 and brac in close_brac and open_brac.find(holder[-1]) == close_brac.find(brac):
            holder.pop()


    if len(holder) == 0:
        return True
    return False

print(test("()"))
print(test("()[]{}"))
print(test("([)]"))
print(test("{[]}"))

# 11 Merge Two Sorted Linked Lists

class LL_Node(object):
#     """Node in a Linked List"""

    def __init__(self, data):
        self.data = data
        self.next = None

    def print_LL(self):

        current = self

        while current is not None:
            print(current.data)
            current = current.next

class LinkedList(object):
    """Linked List"""

    def __init__(self):
        self.head = None
        self.tail = None

    @staticmethod
    def mergeTwoNodes(a, b):
        if a and b:
            if a.data > b.data:
                a, b = b, a
            a.next = LinkedList.mergeTwoNodes(a.next, b)


        return a or b




listA_node1 = LL_Node(2)
listA_node2 = LL_Node(6)
listA_node3 = LL_Node(7)

listA_node1.next = listA_node2
listA_node2.next = listA_node3

listB_node1 = LL_Node(1)
listB_node2 = LL_Node(3)
listB_node3 = LL_Node(8)

listB_node1.next = listB_node2
listB_node2.next = listA_node3

LinkedList.mergeTwoNodes(listA_node1, listB_node1)
# listB_node1.print_LL()
# ^ bug in static method where last node keeps printing data

# three types of methods
# 1. Static method
# 2. Class method (instead of taking self, I would take in Class itself)
# 3. Instance method (everything I've been writing)


# 12 Remove Duplicates from Sorted Array

def no_dupes(lst):
    """Remove dupes in place and return length of new list"""

    lst = set(lst)
    return (len(lst))

print(no_dupes([0,0,1,1,1,2,2,3,3,4]))
print('')

# 13 Maximum Subarray

def max_subarray(nums):

    for i in range(1, len(nums)): #range(1, 9)
        # print("we are on i", i)
        if nums[i-1] > 0:
            nums[i] += nums[i-1]
            print(nums)
    return max(nums)

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
print('')



def count_and_say(n):

    s = '1'

    for x in range(n-1): # range 0 to 4 means 0 to 3
        let = s[0]
        temp = ''
        count = 0
        # print(let, temp, count)

        for l in s:
            if let == l:
                count = count + 1
                # print(count)
            else:
                temp += str(count)+let
                let = l
                count = 1
                # print(count)

        temp += str(count)+let
        s = temp

    return s


print(count_and_say(5)) # 111221

# 1. 1
# 2. 11
# 3. 21
# 4. 1211
# 5. 111221


def combinationSum(candidates, target):
    def dfs(candidates, start, target, path, res):
        if target == 0:
            return res.append(path + [])
            
        for i in range(start, len(candidates)):
            if target - candidates[i] >= 0:
                path.append(candidates[i])
                dfs(candidates, i, target - candidates[i], path, res)
                path.pop()
    res = []
    dfs(candidates, 0, target, [], res)
    return res

print(combinationSum([5,4,2,1], 10))

def climbing_stairs_recursively(n):
    """You are climbing a stair case. It takes n steps to reach to the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can 
    you climb to the top? Given n will be a positive integer."""

    if n == 0 or n == 1:
        return 1    

    return climbing_stairs_recursively(n-1) + climbing_stairs_recursively(n-2)



print(climbing_stairs_recursively(4))


def fact(n):
    """Find n! factorial using recursion."""

    if n == 0:
        return 1

    elif n >= 1:
        return n * fact(n-1)

print(fact(4))
print('')


def single_num(lst):

    dict = {}

    for num in lst:
        dict[num] = dict.get(num, 0) + 1

    for num, count in dict.items():
        if count == 1:
            return num


print(single_num([2,2,1]))
print(single_num([4,1,2,1,2]))

# Design a stack that supports push, pop, top, and retrieving the minimum 
# element in constant time.

class MinStack(object):

    def __init__(self):

        self._stack = []
        

    def push(self, x):

        self._stack.append(x)
       
    def pop(self):
        
        return self._stack.pop()

    def top(self):
        
        return self._stack[-1]
        

    def getMin(self):

        return min(self._stack)

my_stack = MinStack()
my_stack.push(4)
my_stack.push(10)
my_stack.push(6)
my_stack.push(1)
my_stack.top()
my_stack.getMin()
       

def majority_element(lst):

    dict = {}

    for num in lst:
        dict[num] = dict.get(num, 0) + 1

    maximum = max(dict.values())

    for key, value in dict.items():
        if value == maximum:
            return key

print(majority_element([3,2,3]))
print(majority_element([2,2,1,1,1,2,2]))
print('')


# def excel_sheet(letters):

#     dict = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 
#     'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 
#     'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}

#     if len(letters) == 1:
#         return dict[letters]

#     elif 


# print(excel_sheet('P')) #16
# print(excel_sheet('AB')) #28
# print(excel_sheet('ZY')) #701


def count_numbers(num): 

    new_list = []     
    num = str(num)      
    counter = 0     

    current_value = 0 


    for value in num:         
        if current_value == 0:             
            current_value = value             
            counter += 1         
        elif current_value == value:
            counter += 1 

        elif value != current_value:
            new_list.append(counter)
            counter = 0
            new_list.append(current_value)
            counter += 1
            current_value = value

    new_list.append(counter)
    new_list.append(current_value)
            

    return new_list
                         
          
print(count_numbers(112233))


def house_robber(lst):

    sum_odd = sum(lst[::2])
    sum_even = sum(lst[1::2])

    return max(sum_odd, sum_even)

print(house_robber([1,2,3,1]))
print(house_robber([2,7,9,3,1]))
print('')



def move_zeros(lst):

    for num in lst:
        if num == 0:
            lst.remove(num)
            lst.append(num)
        else:
            continue

    return lst

print(move_zeros([0,1,0,3,12])) # [1,3,12,0,0]


def isPowerOfThree(n):
       
    if n < 1:
        return False
    elif n == 1:
        return True

    val = 1
    while val < n:
        val *= 3
        if val == n:
            return True
    return False

print(isPowerOfThree(27)) #T
print(isPowerOfThree(0)) #F
print(isPowerOfThree(9)) #T
print(isPowerOfThree(45)) #F


# First Unique Character in a String

# def first_unique(string):
#     """Given a string, find the first non-repeating character in it and return 
#     it's index. If it doesn't exist, return -1."""

#     holder = ''

#     for letter in string:
#         if holder == '':
#             holder = letter
#             continue


# print(first_unique("leetcode")) #0
# print(first_unique("loveleetcode")) #2

def sort_colors(lst): #leetcode Sort Colors Medium

    for i in range(len(lst) - 1):  # for i in [0, 1, 2, 3, 4, 5]

            # keep track of whether we made a swap
            made_swap = False

            for j in range(len(lst) - 1 - i): # for j in [0, 1, 2, 3, 4, 5]
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
                    made_swap = True

            if not made_swap:
                # if no swap, list already sorted
                break

    return lst 

print(sort_colors([2,0,2,1,1,0])) #[0,0,1,1,2,2]
print('')




def left_rotation(how_many_num, rotate_num):

    lst_1 = range(1, how_many_num + 1)
    lst_2 = []

    for num in lst_1:
        lst_2.append(num)

    # lst_2 = [1,2,3,4,5]

    a = lst_2[rotate_num::]
    b = lst_2[:rotate_num]

    return a+b


print(left_rotation(5, 4)) #[5,1,2,3,4]
print(left_rotation(5, 2)) 
print(left_rotation(5, 3))


def subdomain(lst):

    dictionary = {}

    for x in lst:
        visits_site = x.split(' ')
        visits = visits_site[0]
        site = visits_site[1]
        print(visits)
        print(site)



        if site in dictionary:
            dictionary[site] += visits
        elif site not in dictionary:
            dictionary[site] = visits

        # while len(site) != 0:
        split_site = site.split(".")
        del(split_site[0])
        split_site = '.'.join(split_site)

        print(split_site)



    print(dictionary)




print(subdomain(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))




def pow(x, n):

    if n > 0:

        i = 0
        answer = 1

        while i != n:
            answer = float(answer) * float(x)
            i = i + 1

        return answer

    else:
        x = float(1/x)
        n = -(n)

        i = 0
        answer = 1


        while i != n:
            answer = float(answer) * float(x)
            i = i + 1

        return answer


print(pow(2.000, 10)) 
print(pow(2.100, 3)) 
print(pow(2.000, -2)) 
print('')

# def permutations(lst):

#     dict = {}

#     for 


# print(permutations([1,2,3]))

def rotate_image(lst):

    return (list(zip(*(lst[::-1]))))

print(rotate_image([
  [1,2,3],
  [4,5,6],
  [7,8,9]
]))

#[
#  [7,4,1],
#  [8,5,2],
#  [9,6,3]
# ]

# input [1,2,3,4,5,6,7,8,9]
# output [7,4,1,8,5,2,9,6,3]

print(rotate_image([
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]))

# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]


def position_of_element(lst, target):

    if target not in lst:
        return [-1,-1]

    answer = []

    for i, num in enumerate(lst):
        if num == target:
            answer.append(i)

    return answer


print(position_of_element([5,7,7,8,8,10], 8)) #[3,4]
print(position_of_element([5,7,7,8,8,10], 6)) #[-1,-1]
print('')

def valid_sudoku(lst):

    # check if rows are unique 


    # for row in lst:

    #     i = 0
    #     row_checker = []

    #     if row[i] not in row_checker and row[i].isnumeric():
    #         row_checker.append(row[i])
    #         i = i + 1

    #     elif row[i] == ".":
    #         i = i + 1

    #     elif row[i] in row_checker:
    #         return False

    # row_valid = True


    # check if columns are unique
    # x = 0
    # while x != 9:

    #     column_checker = []

    #     for row in lst:
    #         if row[x] not in column_checker and row[x].isnumeric():
    #             column_checker.append(row[x])
            
    #         elif row[x] == ".":
    #             continue

    #         elif row[x] in column_checker:
    #             return False

    #     x = x + 1

    # column_valid = True


    # check if sub-boxes are unique

    full_list = []

    for row in lst:
        full_list.extend(row)

    dictionary = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}







print(valid_sudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
])) # True


print(valid_sudoku([
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
])) # False b/c 8 repeats in left column

print(valid_sudoku([
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["2",".",".",".","6",".",".",".","3"],
  ["4","9",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
])) # False b/c 8 repeats in left column


# rectangle overlap

def is_overlap(rec1, rec2):

    # if rec1[2] <= rec2[0] or rec2[2] <= rec1[0] or rec1[3] <= rec2[1] or rec2[3] <= rec1[1]:
    #     return False
    # return True

    return rec1[0] < rec2[2] and rec2[0] < rec1[2] and rec1[1] < rec2[3] and rec2[1] < rec1[3]


print(is_overlap([0,0,2,2], [1,1,3,3])) #true
print(is_overlap([0,0,1,1], [1,0,2,1])) #false

print(is_overlap([-3,-2,1,1], [-1,0,2,1])) #true


def decode_ways(string):

    options = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

    if len(string) == 1:
        return 1

    if len(string) == 2 and string[1] == "0":
        return 1

    if len(string) == 2 and string[0] == '1':
        return 2

    if int(string) in range(21, 27):
        return 2

    count = 1
    if len(string) == 3:
        if int(string[1:]) in options:
            count += 1
        if int(string[0:2]) in options:
            count += 1

    return count




print(decode_ways('12'))
print(decode_ways('226'))
print('')


# Container with most water

def most_water(lst):

    maximum = 0
    
    for i, data in enumerate(lst):
        if i > len(lst) - 2:
            break

        else:

            j = i + 1

            while j != len(lst):
                
                min_height = min(lst[i], lst[j])
                distance = j - i
                volume = min_height * distance

                if volume > maximum:
                    maximum = volume

                j = j + 1

    return maximum

print(most_water([1,8,6,2,5,4,8,3,7]))
print('')


# def wordBreak(s, words):

#     ok = [True]

#     print(ok)

#     for i in range(1, len(s)+1):
#         ok += any(ok[j] and s[j:i] in words for j in range(i)),

#     return ok[-1]

# print(wordBreak("leetcode", ["leet", "code"])) # true
# print(wordBreak("applepenapple", ["apple", "pen"])) # true
# print(wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])) # false


# try to recode the above without comprehension
# def wordBreak(s, words):

#     ok = [True]

#     print(ok)

#     for i in range(1, len(s)+1):
#         for j in range(i):
#             if ok[j] and s[j:i] in words:
#                 ok += ok[j] and s[j:i]

#     return ok[-1]

# print(wordBreak("leetcode", ["leet", "code"])) # true
# print(wordBreak("applepenapple", ["apple", "pen"])) # true
# print(wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])) # false


# zigzag conversion

def zigzag(string, rows):

    dictionary = {}

    for x in range(1, rows+1):
        dictionary[x] = []

    string = list(string)

    i = 1
    direction = 'up'

    while string:
        n = string.pop(0)
        # print(i)
        dictionary[i] += n

        if i < rows and direction == 'up':
            i = i + 1
        elif i == rows:
            i = i - 1
            direction = 'down'

        elif i == 1 and direction == 'down':
            i = i + 1
            direction = 'up'
        elif i < rows and direction == 'down':
            i = i - 1


    answer = []
    for a in dictionary.values():
        answer.extend(a)  

    return ''.join(answer)


print(zigzag("PAYPALISHIRING", 3))
print(zigzag("PAYPALISHIRING", 4))


# swap nodes in pairs
# Given a linked list, swap every two adjacent nodes and return its head.
# Given 1->2->3->4, you should return the list as 2->1->4->3

# class Node(object):

#     def __init__(self, data):
#         self.data = data
#         self.next = None 

# class LL(object):

#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def append(self, data):

#         new_node = Node(data)

#         if self.head is None:  
#             self.head = new_node 

#         if self.tail is not None: 
#             self.tail.next = new_node

#         self.tail = new_node

#     def swap_pairs(self):

#         current = self.head 

#         while current:
#             if current == self.head:
#                 current.next = self.head
#                 current.next.next = current

#     def print_list(self):

#         current = self.head

#         while current is not None:
#             print(current.data)
#             current = current.next

# test_ll = LL()
# test_ll.append(1)
# test_ll.append(2)
# test_ll.append(3)
# test_ll.append(4)
# test_ll.swap_pairs()
# test_ll.print_list()


def merge_intervals(lst):

    i = 0
    j = 1

    count = 0

    while count != len(lst):

        if lst[j][0] <= lst[i][1]:
            lst[i] = [lst[i][0], lst[j][1]]
            del lst[j]
            count = count + 1

        else:
            i = i + 1
            j = i + 1
            count = count + 1


    return lst



print(merge_intervals([[1,3],[2,6],[8,10],[15,18]])) #[[1,6],[8,10],[15,18]]
print(merge_intervals([[1,4],[4,5]])) #[[1,5]]

print(merge_intervals([[1,4],[6,10],[9,11],[14,19]])) 


def restore_IP_adress(string):

    made_into_lst = list(string)
    dot = '.'
    answer = []

    answer.append(made_into_lst[0:3])
    answer[0].extend(dot)
    answer[0].extend(made_into_lst[3:6])
    answer[0].extend(dot)
    answer[0].extend(made_into_lst[6:8])
    answer[0].extend(dot)
    answer[0].extend(made_into_lst[8:])

    answer.append(made_into_lst[0:3])
    answer[1].extend(dot)
    answer[1].extend(made_into_lst[3:6])
    answer[1].extend(dot)
    answer[1].extend(made_into_lst[6:9])
    answer[1].extend(dot)
    answer[1].extend(made_into_lst[9:])

    for x in answer:
        ''.join(x)
        print(x)


    # print(answer)


print(restore_IP_adress('25525511135')) #["255.255.11.135", "255.255.111.35"]


print('space')
print('')

# def version(v_1, v_2):

#     for i_1, x in enumerate(v_1):
#         if x == '.':
#             index_1 = i_1
#             break  


#     for i_2, y in enumerate(v_2):
#         if y == '.':
#             index_2 = i_2
#             break


#     if v_1[:index_1] > v_2[:index_2]:
#         return 1

#     elif v_1[:index_1] < v_2[:index_2]:
#         return -1

#     else:






# print(version('0.1', '1.1')) # -1
# print(version('1.0.1', '1.0')) # 1
# print(version('1.0.1.1', '1.0.1')) # 1
# print(version('3.0.1.1', '21.0.1')) # -1

# print(version('1.0.1', '1.')) # 1



#Write a function to find all the 10-letter-long sequences (substrings) 
#that occur more than once in a DNA molecule.

def repeated_dna(string):

    length_of_str = len(string)
    make_to_lst = list(string)
    holder = []
    i = 0
    j = 0

    dictionary = {}

    while i != length_of_str - 9:
        while j < i + 10:
            holder.append(make_to_lst[j])
            j = j + 1

        if ''.join(holder) not in dictionary.keys():
            dictionary[''.join(holder)] = 1
        else:
            dictionary[''.join(holder)] += 1
        holder = []    
        i = i + 1
        j = i

    answer = []

    for k, v in dictionary.items():
        if v >= 2:
            answer.append(k)


    return answer

print(repeated_dna("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
#["AAAAACCCCC", "CCCCCAAAAA"]
print('')


def elimination_game(n):

    lst = []

    for x in range(1,n+1):
        lst.append(x)


    direction = 'up'

    while len(lst) != 1:

        if direction == 'up':
            lst = lst[1::2]
            direction = 'down'
            # print(lst)
        elif direction == 'down':
            lst = lst[::-1]
            direction = 'up'
            # print(lst)

    return lst


print(elimination_game(9))
print(elimination_game(10))
print(elimination_game(11))
print(elimination_game(12))
print(elimination_game(13))

# 1,2,3,4,5,6,7,8,9
# 2,4,6,8
# 2,6
# 6 

# 1,2,3,4,5,6,7,8,9,10
# 2,4,6,8,10
# 4,8
# 8


# 1,2,3,4,5,6,7,8,9,10,11
# 2,4,6,8,10
# 4,8
# 8

# 1,2,3,4,5,6,7,8,9,10,11,12
# 2,4,6,8,10,12
# 2,6,10
# 6

# 1,2,3,4,5,6,7,8,9,10,11,12,13
# 2,4,6,8,10,12
# 2,6,10
# 6

# Reconstruct Original Digits from English

def digits_from_eng(string):

    dictionary = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five':5, 'six': 6, 'seven':7, 'eight': 8, 'nine': 9}

    pass


print(digits_from_eng("owoztneoer"))
print(digits_from_eng("fviefuro"))


def assign_cookies(children, cookies):

    answer = 0

    for num in cookies: 
        if num in children:
            answer += 1
            for i, child in enumerate(children):
                if child == num:
                    del(children[i])
                    break

    return answer



print(assign_cookies([1,2,3], [1,1])) #1
print(assign_cookies([1,2], [1,2,3])) #2
print('')


def keys_and_rooms(rooms):

    current_room = 0
    next_room = current_room + 1

    while current_room != len(rooms)-1:

        if next_room not in rooms[current_room]:
            return False

        elif next_room in rooms[current_room]:
            current_room = current_room + 1
            next_room = current_room + 1

    return True


print(keys_and_rooms([[1],[2],[3],[]]))
print(keys_and_rooms([[1,3],[3,0,1],[2],[0]]))



def practice_dict(word):

    dictionary = {}

    for char in word:
        if char not in dictionary.keys():
            dictionary[char] = 1
        else:
            dictionary[char] += 1

    return dictionary


print(practice_dict("elephant"))


# lambda practice
# lambda functions are single-use throw-away functions

add5 = lambda x: x + 5
print(add5(7))


list1 = [("eggs", 5.25), ("honey", 9.70), ("carrots", 7.43)]
list1.sort(key = lambda x: x[0])
print(list1)


list2 = [("eggs", 5.25), ("honey", 9.70), ("carrots", 7.43)]
list2.sort(key = lambda x: x[1])
print(list2)


all_nums = [1,2,3,4,5,6]
even_nums = list(filter(lambda x: x%2 == 0, all_nums))
print(even_nums)


orig_nums = [1,2,3,4,5,6]
squared = list(map(lambda x: x ** 2, orig_nums))
print(squared)


starts_with_J = lambda x: True if x.startswith('J') else False
print(starts_with_J("Jessica"))


wordb4 = lambda s, w: s.split()[s.split().index(w)-1] if w in s else None
sentence = "Four score and seven years ago"
print(wordb4(sentence, 'seven'))


# list comprehension practice
# new_list = [expression for_loop_one_or_more conditions]

a = ['green', 'yellow', 'red']
b = [x.upper() for x in a]
print(b)


list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]

common_num = [a for a in list_a for b in list_b if a == b]
print(common_num)

# for a in list_a:
#     for b in list_b:
#         if a == b:
#             print(a)


# n kids are sitting in a circle
# k toy available to distribute
# i position to start from
# which kid will get the last toy?

def kids_and_toys(n,k,i):


    while k > 0:
        k -= 1
        if i > n:
            i = 1
        else:
            i += 1

    return i



print(kids_and_toys(3,5,1)) #2
print(kids_and_toys(4,3,3)) #1


def palindrome_number(num):

    string_num = str(num)

    i = 0
    j = len(string_num)-1

    while i < j:
        if string_num[i] == string_num[j]:
            i += 1
            j -= 1
        else:
            return False

    return True



print(palindrome_number(121)) #true
print(palindrome_number(-121)) #false
print(palindrome_number(10)) #false
print(palindrome_number(1001)) #true


def two_sum_attempt(nums, target):

    for index, num in enumerate(nums):
        print(index, num)
        needed_num = target - num
        print(needed_num)
        if needed_num in nums:
            index_needed_num = nums.index(needed_num)
            if index_needed_num != index:
                return([index, index_needed_num])


print(two_sum_attempt([2,7,11,15], 9)) #[0,1]
print(two_sum_attempt([3,2,4], 6)) #[1,2]


#You are given two non-empty linked lists representing two non-negative integers. 
#The digits are stored in reverse order and each of their nodes contain a single 
#digit. Add the two numbers and return it as a linked list.

#You may assume the two numbers do not contain any leading zero, except the number
#0 itself.

# Definition for singly-linked list.
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    """Linked List"""

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """append node with data to end of list"""

        new_node = Node(data)

        if self.head is None: 
            self.head = new_node 

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node

    def print_list(self):
        """print all items in the list"""

        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

class solution(object):

    def add_two_reversed_ll(self, l1, l2):

        answer = LinkedList()

        # answer = []

        current_1 = l1.head
        current_2 = l2.head

        carry = 0

        while current_1 or current_2:

            if current_1 == None:
                answer.append(current_2.data)
                current_2 = current_2.next

            elif current_2 == None:
                answer.append(current_1.data)
                current_1 = current_1.next

            elif current_1 and current_2:

                addition = current_1.data + current_2.data

                if addition < 10 and carry == 1:
                    answer.append(addition + 1)
                    carry = 0
                elif addition < 10 and carry == 0:
                    answer.append(addition)
                elif addition > 9 and carry == 1:
                    answer.append((addition-10)+1)
                elif addition > 9 and carry == 0:
                    answer.append(addition-10)
                    carry = 1

                current_1 = current_1.next
                current_2 = current_2.next

        print(answer.print_list())



        # l1_int = []
        
        # current_1 = l1.head
        
        # while current_1 != None:
        #     l1_int.append(current_1.data)
        #     current_1 = current_1.next
            
        # l2_int = []
        
        # current_2 = l2.head
        
        # while current_2 != None:
        #     l2_int.append(current_2.data)
        #     current_2 = current_2.next


        # l1_int = l1_int[::-1]
        # l2_int = l2_int[::-1]

        # l1_int = [str(i) for i in l1_int] 
        # l1_int = int("".join(l1_int))

        # l2_int = [str(i) for i in l2_int] 
        # l2_int = int("".join(l2_int))

        # int_answer = l1_int + l2_int 



# ll_1 = LinkedList()
# ll_1.append(2)
# ll_1.append(4)
# ll_1.append(3)
# ll_2 = LinkedList()
# ll_2.append(5)
# ll_2.append(6)
# ll_2.append(4)

# ll_1 = LinkedList()
# ll_1.append(2)
# ll_1.append(4)
# ll_1.append(3)
# ll_2 = LinkedList()
# ll_2.append(5)
# ll_2.append(6)
# ll_2.append(4)
# ll_2.append(2)

ll_1 = LinkedList()
ll_1.append(2)
ll_1.append(4)
ll_1.append(3)
ll_1.append(2)
ll_1.append(3)
ll_2 = LinkedList()
ll_2.append(5)
ll_2.append(6)
ll_2.append(4)


test1 = solution()

print(test1.add_two_reversed_ll(ll_1, ll_2))
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807

print("BREAK")

import math

def median_two_sorted_arrays(nums1, nums2):

    new_array = sorted(nums1 + nums2)
        
    if len(new_array) % 2 == 0:
        first_num_index = int(len(new_array)/2) - 1
        second_num_index = first_num_index + 1
        return((new_array[first_num_index]+new_array[second_num_index])/2)
        
    else:
        return(new_array[math.ceil(len(new_array)/2)]-1)

print(median_two_sorted_arrays([1,3], [2]))
print(median_two_sorted_arrays([1,2], [3,4]))



def longest_common_prefix(lst):

    lst.sort(key=len)
    print(lst)

print(longest_common_prefix(['flower', 'flow', 'flight']))


print("KEEPTRUCKIN")

def goodSegment(badNumbers, l, r):

    sorted_badNumbers = sorted(badNumbers)

    longest_segment = sorted_badNumbers[0]-l

    print(sorted_badNumbers)

    for num in range(1, len(sorted_badNumbers)):
        
        if sorted_badNumbers[num]-(sorted_badNumbers[num-1]+1) > longest_segment and sorted_badNumbers[num]<r:
            longest_segment = sorted_badNumbers[num]-(sorted_badNumbers[num-1]+1)

    if r - sorted_badNumbers[-1] > longest_segment:
        longest_segment = r - sorted_badNumbers[-1]
    if r < sorted_badNumbers[-1] and r - sorted_badNumbers[-2] > longest_segment:
        longest_segment = r - sorted_badNumbers[-2]


    return longest_segment

print(goodSegment([37, 7, 22, 15, 49, 60], 3, 48)) #14
print(goodSegment([8, 6, 20, 12], 1, 30)) #10
print(goodSegment([5, 4, 2, 15], 1, 10)) #5

print("BREAK")

def jobOffers(scores, lowerLimits, upperLimits):

    answer = []
    count = 0

    for x in range(len(lowerLimits)):
        # limit_pairs = [lowerLimits[x], upperLimits[x]]
        # print(limit_pairs)
        for score in scores:
            # print(score)
            if score >= lowerLimits[x] and score <= upperLimits[x]:
                count += 1
                # print(count)
        answer.append(count)
        count = 0

    return answer


print(jobOffers([1, 3, 5, 6, 8],[2] ,[6])) #[3]
print(jobOffers([4,8,7],[2,4],[8,4])) #[3, 1]


def transpose_list(list_of_lists):

    return [list(row) for row in zip(*list_of_lists)]

print(transpose_list([[1, 4, 7], [2, 5, 8], [3, 6, 9]]))
#[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def pal(x):

    if x < 0:
        return False
    else:
        make_list = [int(y) for y in str(x)]

        reverse_list = make_list[::-1]

        if make_list == reverse_list:
            return True
        else:
            return False


print(pal(121)) #True
print(pal(-121)) #False
print(pal(10)) #False

print('BREAK-----------')

def isValid(s):

        
    holder = []
    dict = {'(':')','[':']','{':'}'}
    
        
    if len(s) == 0:
        return True
        
    if len(s) < 2:
        return False
        
    for x in s:
        if x in dict.keys():
            holder.append(x)
        elif x in dict.values() and len(holder) > 0:
            for key, value in dict.items(): 
                if x == value and holder[-1] == key:
                    holder.pop()
                elif x == value and holder[-1] != key:
                    holder.append(x)
        elif x in dict.values() and len(holder) == 0:
            return False
            
    if len(holder) == 0:
        return True
    else:
        return False
        
print(isValid('[])'))
print(isValid('()'))


# https://leetcode.com/problems/shortest-distance-to-a-character/
def shortest_dist_to_char(s, c):

    answer = []

    c_positions = []

    for i, letter in enumerate(s):
        if letter == c:
            c_positions.append(i)

    for i, letter in enumerate(s):
        shortest_dist = len(s)
        for num in c_positions:
            distance = abs(i-num)
            if distance < shortest_dist:
                shortest_dist = distance
        answer.append(shortest_dist)

    return answer

print(shortest_dist_to_char("loveleetcode", "e"))


# https://leetcode.com/problems/single-number/
def single_number(lst):

    dictionary = {}

    for num in lst:
        if num in dictionary.keys():
            dictionary[num] +=1
        else:
            dictionary[num] = 1

    for key, values in dictionary.items():
        if values == 1:
            return key

print(single_number([2,2,1])) #1
print(single_number([4,1,2,1,2])) #4











