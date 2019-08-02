def rev_string_recursively(string):
    """reverse string recursively"""

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

# 5 
# 4 + 5
# 3 + 4
# 4 + 3
# 1 + 2
# 1



def factorial(n):

    if n == 1:
        return 1


    return factorial(n-1) * n


print(factorial(3)) #1*2*3 = 6
print(factorial(5)) #1*2*3*4*5 = 120


def find_uppercase(string, index=0):
    """find the first uppercase character"""

    if string[index].isupper():
        return string[index]

    if index == len(string) - 1:
        return "No uppercase character found"

    return find_uppercase(string, index + 1)


print(find_uppercase('heyThere'))
print(find_uppercase('HeyThere'))
print(find_uppercase('heythere'))


def string_length(string):

    if string == '':
        return 0

    return 1 + string_length(string[1:])

print(string_length("hey"))
print(string_length("hello"))


def count_consonants(string):
    """consonant is a letter that is not a vowel"""

    vowel = 'aeiou'

    if string == '':
        return 0

    if string[0].lower() not in vowel and string[0].isalpha():
        return 1 + count_consonants(string[1:])
    else:
        return count_consonants(string[1:])


print(count_consonants("hey"))
print(count_consonants("hello"))

def product(x, y):

    if y == 0:
        return 0

    return x + product(x, y-1)


print(product(5, 2))
print(product(3, 6))

# Here’s how you do that by threading it through each recursive call 
#(i.e. passing the updated current state to each recursive call as arguments):
def sum_recursive(current_number, accumulated_sum):
 
    if current_number == 11:
        return accumulated_sum

    else:
        return sum_recursive(current_number + 1, accumulated_sum + current_number)


print(sum_recursive(1, 0))

# Here’s how you maintain the state by keeping it in global scope:

# Global mutable state
current_number = 1
accumulated_sum = 0


def sum_recursive():
    global current_number
    global accumulated_sum
    # Base case
    if current_number == 11:
        return accumulated_sum
    # Recursive case
    else:
        accumulated_sum = accumulated_sum + current_number
        current_number = current_number + 1
        return sum_recursive()

print(sum_recursive())


# MIT Tower problem

def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):

    if n == 1:
        printMove(fr, to)

    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)


print(Towers(4, 'a', 'b', 'c'))


def isPalindrome(s):

    def toChars(s):
        s = s.lower()
        answer = ''

        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                answer = answer + c
        return answer

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))

print(isPalindrome('asdfdsa')) # True
print(isPalindrome('asdfda')) # False
print(isPalindrome('asdffdsa')) # True


print("######")

def count_cons(s):
    """count number of non vowel letters in string"""

    if len(s) == 0:
        return 0

    # count = 0
    vowels = 'aeiou'

    if s[0] not in vowels:
        return 1 + count_cons(s[1:])
    else:
        return count_cons(s[1:])

print(count_cons('geekforgeeks'))




# Write a function that takes a list of integers, and finds the maximum of the 
# list using recursion.

print("HERE")

def find_max(lst):

    if len(lst) == 1:
        return lst[0]
    else:
        return max(lst[0], find_max(lst[1:]))

print(find_max([2,5,7,1,8,3]))

print("END HERE")

# 2, [5,7,1,8,3]
# 5, [7,1,8,3]
# 7, [1,8,3]
# 1, [8,3]
# 8, [3]

# [2,5,10,7,1]
# 2, [5,10,7,1]
# 5, [10,7,1]
# 10, [7,1]
# 7, [1]

# Write a function that prints out each element in a given list using recursion.

def print_each(lst):

    if len(lst) == 0:
        return ""             
    else:              
        print(lst[0])  

        return print_each(lst[1:])

print(print_each([4,5,2,7,1]))

# Write a function that prints out the integers 1 through 5 using recursion.

current_number = 1

def print_to_5_global():

    global current_number

    if current_number == 6:
        return ""

    else:
        print(current_number)
        current_number += 1

        return print_to_5_global()


print(print_to_5_global())


def print_to_n(n, current_number):

    if current_number == n+1:
        return ""

    else:
        print(current_number)

        return print_to_n(n, current_number+1)



print(print_to_n(10, 1))


doubled_lst = []

def doubled(lst):


    if len(lst) == 0:
        return doubled_lst

    else:
        doubled_lst.append(lst[0] * 2)
        return doubled(lst[1:])


print(doubled([3,5,10]))

# import pdb
# pdb.set_trace()

def doubled_by_threading(lst, answer_lst):

    if len(lst) == 0:
        return answer_lst

    else:
        answer_lst.append(lst[0]*2)

        return doubled_by_threading(lst[1:], answer_lst)


print(doubled_by_threading([1,2,3], []))

def no_dupes(lst, holding_lst):
    """True if there is no dupes"""

    if len(lst) == 0:
        return True

    else:
        if lst[0] in holding_lst:
            return False

        elif lst[0] not in holding_lst:
            holding_lst.append(lst[0])

            return no_dupes(lst[1:], holding_lst)


print(no_dupes([2,5,7,10,2], [])) #False
print(no_dupes([2,5,7,10], [])) #True



# function to generate the nth fibb number
# 0, 1, 1, 2, 3, 5, 8, 13, 21 etc
def fibb(n):

    print("running", n)
    if n == 0 or n == 1:
        print("n is 0 or 1")
        return n

    else:
        print("about to run", n, "-2", " , ", n, "-1")
        return fibb(n-2) + fibb(n-1) 


print(fibb(6)) #8

#                        fibb(6)                                 fibb(5)
#             fibb(4)                 fibb(3)           fibb(3)        fibb(2)
#        fibb(2)     fibb(3)     fibb(1)   fibb(2)  fibb(2) fibb(1)   fibb(0) fibb(1)
# fibb(0) fibb(1) fibb(1) fibb(2)
#                       fibb(0) fibb(1)     

# tree traversal
# do this non recursively


memo = {0:0, 1:1}
def fibb_with_memo(n):

    if n in memo.keys():
        return memo[n]

    else:
        return fibb_with_memo(n-2) + fibb_with_memo(n-1)

print(fibb_with_memo(6)) #8

print("Doing Kibb probs")


def kibb(n, k):
    """n is the nth num while k is the number of nums needed to be added before"""

    if n < k-1:
        return 0

    elif n == k-1:
        return 1

    else:
        return sum(kibb(n-x, k) for x in range(1, k+1))

# 0,0,0,1,1,2,4,8,15
print(kibb(0, 4)) 
print(kibb(1, 4))
print(kibb(2, 4))
print(kibb(3, 4))
print(kibb(4, 4))
print(kibb(5, 4))
print(kibb(6, 4))
print(kibb(7, 4))
print(kibb(8, 4))



kibb_memo = {0:1}

def kibb_with_memo(n, k):

    #create initial memo
    for x in range(k):
        kibb_memo[x] = 0

    kibb_memo[k] = 1

    if n in kibb_memo.keys():
        return kibb_memo[n]
    else:
        return sum(kibb_with_memo(x-1, k) for x in range(k+1))

print(kibb(0, 4)) 
print(kibb(1, 4))
print(kibb(2, 4))
print(kibb(3, 4))
print(kibb(4, 4))
print(kibb(5, 4))
print(kibb(6, 4))
print(kibb(7, 4))
print(kibb(8, 4))


def nested_list_sum(lst):

    total = 0

    for element in lst:
        if type(element) == type([]):
            total = total + nested_list_sum(element)
        else:
            total = total + element

    return total


print(nested_list_sum([1, 2, [3,4], [5,6]]))
print(nested_list_sum([1, 2, [3,4, [5,6]]]))


def power(a, b):

    if b == 1:
        return a 

    else:
        return power(a, b-1) * a

print(power(3, 4)) # 81


# def int_to_string(x):

#     pass

# print(int_to_string(123))

# def to_string(n,base):

#    conver_tString = "0123456789ABCDEF"

#    if n < base:
#       return conver_tString[n]
#    else:
#       return to_string(n//base,base) + conver_tString[n % base]

# print(to_string(2835,16))


def min_recursive(lst):

    if len(lst) == 1:
        return lst[0]

    else:
        return min(lst[0], min_recursive(lst[1:]))



print(min_recursive([6,2,8,4,1,10,3])) #1





























