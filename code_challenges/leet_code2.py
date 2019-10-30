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
    print('last index is', last_index)
        
    i = 0
    
    while i < last_index and nums[i] != 0:
        i = i + nums[i]
        print('now on index', i)
        
    if i == last_index:
        return True
    else:
        return False

print(jump_game([2,3,1,1,4])) #true
print(jump_game([3,2,1,0,4])) #false
print(jump_game([3,2,1,3,4])) #false
