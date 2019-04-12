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

class LinkedList(object):
    """Linked List"""

    def __init__(self):
        self.head = None
        self.tail = None

    def mergeTwoLists(self, a, b):
        if a and b:
            if a.data > b.data:
                a, b = b, a
            a.next = self.mergeTwoLists(a.next, b)
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
listB_node2.next = listB_node3





