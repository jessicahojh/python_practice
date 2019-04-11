# function to generate the nth fibb number
# 1, 1, 2, 3, 5, 8, 13, 21 etc

# create an empty list
# if length of list is less than 2, append 1
# else, add the last two numbers and append that sum until length of list is n + 1


def fibb(n):

    lst = []

    while len(lst) < n + 1:

        if len(lst) < 2:
            lst.append(1)

        else:
            lst.append(lst[-1] + lst[-2])

    return lst[-1]

print(fibb(4))
print(fibb(5))
print(fibb(1))


def fibb(n):

    if n == 0 or n == 1:
        return 1
    else:
        return fibb(n-2) + fibb(n-1)

print(fibb(4))
print(fibb(5))
print(fibb(1))


memo = {0:1, 1:1}

def fibb(n):

    if n not in memo:
        memo[n] = fibb(n-2) + fibb(n-1)

    return memo[n]

print(fibb(4))
print(fibb(5))
print(fibb(1))

# (4, 3) ---> 2
# 0, 0, 1, 1, 2, 4, 7, 13 

def kibb(n, k):

    if n < k - 1:
        return 0

    elif n == 2:
        return 1

    else:
        return sum(kibb(n-x, k) for x in range(1, k + 1))

print(kibb(0, 3))
print(kibb(1, 3))
print(kibb(2, 3))
print(kibb(3, 3))
print(kibb(4, 3))



