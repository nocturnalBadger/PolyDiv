'''
A script for finding polydivisible numbers for n-base
'''

BASE = 8

'''
Convert a number to an int given that number as a string in the given base
Base key is a string listing each of the digits in the given base in order;
for example: '0123456789' for base ten or '0123456789abcdef' for base sixteen.
'''
def fromBase(baseKey, value):
    result = 0
    base = len(baseKey)
    i = len(value) - 1
    while i >= 0:
        multiplier = base**i
        digitValue = baseKey.index(value[-(i+1)])
        result += digitValue * multiplier
        i -= 1
    return result

'''
Generate a base key (described above) for a given n-base
Returns a string of unique unicode characters.
It doesn't really matter what the characters are meant to represent.
Later we can convert them back to their unicode index using ord() to get the gist of the value.
'''
def baseNKey(n):
    key = ''
    for c in [chr(i) for i in range(n)]:
        key += c
    return key

'''
Find all the permutations of a given string
Returns a set object with n! items
'''
def permutations(input):
    if (len(input) == 1):
        return input[0]
    perms = set()
    for i, sub in enumerate(permutations(input[1:])):
        j = 0
        while j <= len(input):
            perms.add(sub[:j] + input[0] + sub[j:])
            j += 1
    return perms

'''
Check if a given string meets the criteria for being a polydivisible number
Assumes the input is a string where each number in the base occurs once
Requires the basekey for the base being checked (see above)

The number is polydivisible if the substring of the first i digits are divisible by i
(first 2 digits are divisible by 2, first 3 by 3, etc. up to the length)

Note that even though we're working in different bases, 
we're still checking the first TWO digits for divisibility by the number TWO (and so on)
'''
def check(baseKey, string):
    for i, digit in enumerate(string):
        substr = string[:i+1]
        subVal = fromBase(baseKey, substr)
        if (subVal % (i + 1) != 0):
            return False
    return True


bk = baseNKey(BASE)
for p in permutations(bk):
    if check(bk, p):
        print([ord(x) for x in p])