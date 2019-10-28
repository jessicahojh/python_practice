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