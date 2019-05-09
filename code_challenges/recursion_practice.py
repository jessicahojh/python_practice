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
# 5-1 + 5
# 4-1 + 4
# 3-1 + 3
# 2-1 + 2
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
















