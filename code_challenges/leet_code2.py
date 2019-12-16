# a-z   01-26
# aa-az 27-52
# ba-bz 53-78
# ca-cz
# da-dz
# ...
# aaa-aaz (26x26x26)
# aba-abz 

# (number given)/26 will give you the row
# row divided by 26 will give you how many letters
# 

def excel_table(num):

    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    answer = []

    row = int(num/26)
    remainder = num % 26

    if num < 27:
        answer.append(letters[remainder-1])
    else:
        answer.append(letters[row-1])
        answer.append(letters[remainder-1])

    return answer

print(excel_table(24)) #x
print(excel_table(55)) #bc
print(excel_table(701)) #xy
# print(excel_table(1035)) 

print('')

def longest_substring(s):

    max_length = 0
    holder = []

    for i in range(len(s)-1):
        holder.append(s[i])
        j = i + 1

        while s[j] not in holder:
            holder.append(s[j])
            if j < len(s) - 1:
                j = j + 1
            
        if len(holder) > max_length:
            max_length = len(holder)
        
        holder = []

    return max_length

print(longest_substring('abcabcbb')) #3
print(longest_substring('bbba')) #2
print(longest_substring('bbb')) #1
print(longest_substring('pwwkew')) #3

print('')

def is_anagram(s,t):

    if len(s) != len(t):
        return False

    char_count = {}

    for letter in s:
        if letter not in char_count.keys():
            char_count[letter] = 1
        elif letter in char_count.keys():
            char_count[letter] += 1

    for letter in t:
        if letter not in char_count.keys() or char_count[letter] == 0:
            return False
        elif letter in char_count.keys():
            char_count[letter] -= 1

    return True

print(is_anagram('hello', 'hello')) 
print(is_anagram('hello', 'heloo'))
print(is_anagram('helo', 'hello'))

print('')

def group_anagrams(words):

    grouped = {}

    for word in words:
        to_list_word = list(word)
        to_list_word.sort()
        sorted_word = ''.join(to_list_word)

        if sorted_word not in grouped.keys():
            grouped[sorted_word] = [word]
        elif sorted_word in grouped.keys():
            grouped[sorted_word].append(word)

    return grouped.values()

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

print('')

def is_valid_paren(s):

    stack = []
    pairs = {'(':')', '{':'}', '[':']'}

    for char in s:
        if char in pairs.keys():
            stack.append(char)
        elif char in pairs.values() and char == pairs[stack[-1]]:
            stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False

print(is_valid_paren('({[]})'))
print(is_valid_paren('([]}'))
print(is_valid_paren('({[]}){{'))
print(is_valid_paren('({[]})(){}'))

print('')

def climb_stairs(n):

    if n <=3:
        return n

    ways = [0,1,2,3]

    i = 4
    while i <= n:
        ways.append(ways[i-1] + ways[i-2])
        i = i + 1

    return ways[-1]

print(climb_stairs(1))
print(climb_stairs(2))
print(climb_stairs(3))
print(climb_stairs(4))
print(climb_stairs(5))
print(climb_stairs(6))

print('')

def house_robber(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])

    max_loot_at_nth = [nums[0], max(nums[0], nums[1])]

    i = 2
    while i < len(nums):
        print(max_loot_at_nth)
        max_loot_at_nth.append(
            max(nums[i] + max_loot_at_nth[i-2], max_loot_at_nth[i-1]))
        i = i + 1
    
    print(max_loot_at_nth)
    return max_loot_at_nth[-1]

# print(house_robber([3]))
# print(house_robber([3,4]))
# print(house_robber([5,6,7]))
print(house_robber([4,1,1,7]))
print(house_robber([200,7,100,500]))

print('')

def rob(nums):

    rob1 = 0
    rob2 = 0
    i = 0
    j = 1

    while i < len(nums):
        rob1 += nums[i]
        i = i+2
       
   
    while j < len(nums):
        rob2 += nums[j]
        j = j+2
   
    if rob1 > rob2:
        return rob1
    else:
        return rob2

# print(rob([3]))
# print(rob([3,4]))
# print(rob([5,6,7]))
print(rob([4,1,1,7]))
print(rob([200,7,100,500]))

print('')

def jump_game(nums):

    last_index = len(nums)-1
    # print('last index is', last_index)
        
    i = 0
    
    while i < last_index and nums[i] != 0:
        # print('current index is', i)
        i = i + nums[i]
        if i >= last_index:
            if i >= last_index:
                return True
            else:
                return False
        elif nums[i] == 0:
            return False

print(jump_game([2,3,1,1,4])) #true
print(jump_game([3,2,1,0,4])) #false
print(jump_game([3,2,1,3,4])) #true
print(jump_game([2,0])) #true

print('')

# Longest increasing subsequence
# def lis(nums):

#     longest = 0
    
#     for i in range(len(nums)):
#         print('i is', i)
#         j = i + 1
#         current_longest = 0
#         while nums[j] > nums[i]:
#             print('j is greater than i')
#             current_longest += 1
#             print('current longest is', current_longest)
#             j =+ 1
#             print('j is', j)
#         if current_longest > longest:
#             print('current longest is greater than prev long')
#             longest = current_longest

#     return longest

# print(lis([10,9,2,5,3,7,101,18])) #4

def coin_change(coins, amount):

    coin_count = 0
    coin_combo = sorted(coins)
    coin_left = amount
    largest_coin = len(coins)-1

    print('sorted is', coin_combo)

    while coin_left > 0:
        if coin_combo[largest_coin] == coin_left:
            coin_count += 1
            return coin_count
        elif coin_combo[largest_coin] < coin_left:
            coin_left = coin_left - coin_combo[largest_coin]
            coin_count += 1
            print('coin left now', coin_left)
        elif coin_combo[largest_coin] > coin_left:
            if largest_coin > 0:
                largest_coin -= 1
            else:
                return -1

    return coin_count


print(coin_change([186,419,83,408], 6249))
# print(coin_change([1, 2, 5], 11)) #3
# print(coin_change([2], 3)) #-1

print('break')

def max_sub_array(arr):

    max_sub = arr[0]

    for i, num in enumerate(arr):
        holder = num
        if holder > max_sub:
                max_sub = holder

        for j in range(i+1, len(arr)):
            holder += arr[j]
            if holder > max_sub:
                max_sub = holder

    return max_sub

print(max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))  #6 b/c [4,-1,2,1] has the largest sum
print(max_sub_array([1]))  #1

print('break')

def rotate_arr(arr, k):

    return arr[-k:] + arr[:-k]

print(rotate_arr([1,2,3,4,5,6,7], 1))
print(rotate_arr([1,2,3,4,5,6,7], 2))
print(rotate_arr([1,2,3,4,5,6,7], 3))

print('break')

def move_zeros(arr):

    zero_count = 0
    zero_position = []

    # detect zero's position
    for i, num in enumerate(arr):
        # print(num)
        if num == 0:
            zero_count += 1
            zero_position.append(i)
    
    # reverse zero position
    zero_position = zero_position[::-1]

    # delete the zeros
    for index in zero_position:
        del arr[index]

    # append the zeros back in array
    for num in range(zero_count):
        arr.append(0)

    return arr


print(move_zeros([0,1,0,3,12]))
print(move_zeros([0,0,1]))

print('break')

def third_max_num(arr):
    """Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. 
    The time complexity must be in O(n). """

    if len(set(arr)) < 3:
        return max(arr)

    sorted_arr = sorted(set(arr))
    
    return sorted_arr[-3]

print(third_max_num([3,2,1])) #1
print(third_max_num([10,3,5,7,2])) #5
print(third_max_num([10,3,5,7,2,19])) #7
print(third_max_num([1,2])) #2
print(third_max_num([2,2,3,1])) #1

print('break')

# Find All Numbers Disappeared in an Array

def disappeared(arr):

    answer = []

    for num in range(1, max(arr)):
        if num not in arr:
            answer.append(num)

    return answer

print(disappeared([4,3,2,7,8,2,3,1])) #[5,6]

print('break')

# Given a binary array, find the maximum number of consecutive 1s in this array.

def consecutive_ones(arr):

    max_consecutive = 0
    temp = 0

    for i, num in enumerate(arr):
        if num == 1 and i == len(arr)-1:
            temp += 1
            if temp > max_consecutive:
                max_consecutive = temp

        elif num == 1:
            temp += 1

        elif num == 0:
            if temp > max_consecutive:
                max_consecutive = temp
                temp = 0
            elif temp < max_consecutive:
                temp = 0
            elif temp == max_consecutive:
                temp = 0

    return max_consecutive 

print(consecutive_ones([1,1,0,1,1,1])) #3

print('break')

def height_checker(arr):

    count = 0

    correct_order = sorted(arr)

    for i, num in enumerate(arr):
        if num != correct_order[i]:
            count += 1

    return count

print(height_checker([1,1,4,2,1,3])) #3, Students with heights 4, 3 and the last 1 are not standing in the right positions

print('break')

def words(arr, chars):

    sum_answer = 0

    for word in arr:
        holder = 0
        char_arr = list(chars)
        for letter in word:
            if letter in char_arr:
                holder += 1
                char_arr.remove(letter)
            if holder == len(word):
                sum_answer += len(word)

    return sum_answer

print(words(["cat","bt","hat","tree"], "atach")) #The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6

print('break')

def relative_sort(arr1, arr2):
    """Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  
    Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order."""

    answer = []

    ending = []
    matches = []

    for x in arr1:
        if x not in arr2:
            ending.append(x)
        else:
            matches.append(x)

    for i in arr2:
        for j in matches:
            if j == i:
                answer.append(j)

    ending = sorted(ending)

    return answer + ending


print(relative_sort([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6])) #[2,2,2,1,4,3,3,9,6,7,19]

print('break')

def jewels_stones(j, s):

    counter = 0
    
    for i in s:
        if i in j:
            counter += 1

    return counter

print(jewels_stones("aA", "aAAbbbb")) #3

print('break')

# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

def repeated_element(lst):

    half_length = len(lst)/2

    dictionary = {}

    for num in lst:
        if num not in dictionary.keys():
            dictionary[num] = 1
        else:
            dictionary[num] += 1

    for key, value in dictionary.items():
        if value == half_length:
            return key


print(repeated_element([5,1,5,2,5,3,5,4])) #5

print("break")

def daily_temp(T):

    answer = []
     
    for i, temp in enumerate(T):
        sliced = T[i+1:]
        appended = False
        for index, s in enumerate(sliced):
            if s > temp:
                answer.append(index + 1)
                appended = True
                break
        if appended == False:
            answer.append(0)

    return answer
    
# print(daily_temp([73, 74, 75, 71, 69, 72, 76, 73])) # [1, 1, 4, 2, 1, 1, 0, 0]
print(daily_temp([73, 74, 100, 75, 71, 69, 72, 76, 73])) # [1, 1, 0, 4, 2, 1, 1, 0, 0]


def combine(arrA, arrB, lastIndex):
    indexA  = lastIndex
    indexB = len(arrB)-1
    writeIndex = len(arrA) - 1

    while(indexB >= 0):
        if arrB[indexB] >= arrA[indexA]:
            arrA[writeIndex] = arrB[indexB]
            indexB -= 1
        else:
            arrA[writeIndex] = arrA[indexA]
            indexA -= 1
        writeIndex -= 1

    return arrA

print(combine([1,2,3,4,5,6,-1,-1,-1,-1], [3,4,10,12], 5))

def find(arr):

    currSet = set(arr[0])
    for subArr in arr[1:]:
        newSet = set()
        for j in subArr:
            if j in currSet:
                newSet.add(j)

        currSet = newSet

    return min(newSet)

print(find([[1,3,5,10,20],
            [3,5],
            [5,20,100]])) #3 b/c it is the smallest num that occurred in all three subarrays

# https://leetcode.com/problems/employee-importance/

# class Employee(object):
#     def __init__(self, id, importance, subordinates):
#         # unique id of this employee
#         self.id = id
#         # the importance value of this employee
#         self.importance = importance
#         # the id of direct subordinates
#         self.subordinates = subordinates

# class Solution(object):
#     def getImportance(self, employees, id):

#         employee_dict = {}
#         queue = [id]
#         importance_sum = 0

#         for employee in employees:
#             employee_dict[employee.id] = employee
            
#         while(queue):
#             employee_index = queue.pop(0)
#             employee = employee_dict[employee_index]
#             importance_sum += employee.importance
#             queue.extend(employee.subordinates)
        
#         return importance_sum


# company = Solution()  
# company.getImportance([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1) #11
        
print('BREAK')

def strStr(haystack, needle):
    
    for i, letter in enumerate(haystack):
        if letter == needle[0]:
            isMatch = haystack[i: i+len(needle)] == needle
            if isMatch:
                return i
            
    return -1

print(strStr('hello', 'll')) #2

print("break")

def lengthOfLastWord(s):
    
    word_lst = s.split(' ')

    print(word_lst)
    
    cleaned_word_lst = []
    
    for item in word_lst:
        if item != '':
            cleaned_word_lst.append(item)

    print(cleaned_word_lst)

    if len(cleaned_word_lst) == 0:
        return 0

    return len(cleaned_word_lst[-1])

print(lengthOfLastWord(' '))

def canConstruct(ransomNote, magazine):
    
    dictionary = {}
    
    for letter in magazine:
        if letter not in dictionary.keys():
            dictionary[letter] = 1
        else:
            dictionary[letter] += 1
            
    for item in ransomNote:
        if item not in dictionary.keys():
            return False
        elif item in dictionary.keys():
            dictionary[item] -= 1
            
    for num in dictionary.values():
        if num < 0:
            return False
        
    return True


