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

















