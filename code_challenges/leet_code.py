# Two Sum
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

# Reverse Integer 
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

# Roman to Integer
def rom_int(roman):

    dictionary = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

    lst = []

    for letter in roman:
        lst.append(letter)

    numbers = []

    for letter in lst:
            if letter in dictionary.keys():
                numbers.append(dictionary[letter])

    return numbers


print(rom_int("III"))
print(rom_int("IV"))
print(rom_int("IX"))
print(rom_int("LVIII"))
print(rom_int("MCMXCIV"))

# Longest Common Prefix
def prefix(list):

    pass

print(prefix(["flower","flow","flight"])) # "fl"
print(prefix(["dog","racecar","car"]))   # ""

# 3Sum
def 3_sum(lst):


print(3_sum([-1, 0, 1, 2, -1, -4]))
