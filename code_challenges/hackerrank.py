# https://www.hackerrank.com/challenges/weighted-uniform-string/problem
def weightedUniformStrings(s, queries):

    weights = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10,
               'k':11, 'l':12, 'm':13, 'n':14, 'o':15,'p':16, 'q':17, 'r':18, 's':19, 
               't':20, 'u':21, 'v':22,'w':23, 'x':24, 'y':25, 'z':26}

    substring = ""
    uni_substring = ""

    hashmap = {}

    for i in range(len(s)):
        substring = s[i] 
        if substring != s[i-1]:
            uni_substring = substring 
            hashmap[substring] = weights[substring]
        else:
            uni_substring += substring 
            hashmap[uni_substring] = weights[substring] * len(uni_substring)

    print(hashmap)

    for num in queries:
        if num in hashmap.values():
            print("Yes")
        else:
          print("No")

print(weightedUniformStrings('aaabbbbcccddd', [9,7,8,12,5]))
print(weightedUniformStrings('abccddde', [1,3,12,5,9,10]))

# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

# def rotLeft(a, d):

#     x = []

#     for num in range(1, a+1):
#         x.append(num)

#     if d == len(x)-1:
#         newArr = list(x[-1]) + x[:d]
#         return newArr

#     elif d > len(x):
#         new_d = d - len(x)
#         newArr = x[new_d:] + x[:new_d]
#         return newArr
        
#     else:
#         newArr = x[d:] + x[:d]
#         return newArr

# print(rotLeft(5,4))

# Make Anagram

def makeAnagram(a, b):

  dict1 = {}
  dict2 = {}

  for letter in a:
    if letter in dict1.keys():
      dict1[letter] += 1
    else:
      dict1[letter] = 1

  for letter in b:
    if letter in dict2.keys():
      dict2[letter] += 1
    else:
      dict2[letter] = 1

  print(dict1)
  print(dict2)

  counter = 0

  for letter in dict1.keys():
    if letter not in dict2.keys():
      counter += dict1[letter]
    else:
      if dict1[letter] > dict2[letter]:
        counter += dict1[letter] - dict2[letter]
      elif dict1[letter] < dict2[letter]:
        counter += dict2[letter] - dict1[letter]

  for letter in dict2.keys():
    if letter not in dict1.keys():
      counter += dict2[letter]

  return counter

print(makeAnagram('fcrxzwscanmligyxyvym','jxwtrhvujlmrpdoqbisbwhmgpmeoke')) #30
