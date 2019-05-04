# page 90

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









