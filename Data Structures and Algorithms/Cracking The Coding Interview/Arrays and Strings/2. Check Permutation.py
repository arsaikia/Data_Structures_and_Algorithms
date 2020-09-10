"""
1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.
"""


# Approach 1: Sort and compare
# O(n log(n)) Time | O(n log(n)) Space // n: string length
def isSame(string1, string2):
    if len(string1) != len(string2):
        return False
    string1 = "".join(sorted(string1))
    string2 = "".join(sorted(string2))
    return string1 == string2


# O(n) Time | O(n) Space
def isPermutation(s1, s2):
    # use hashmap to keep count of char occurance
    occurance = {}
    for char in s1:
        if char not in occurance:
            occurance[char] = 1
        else:
            occurance[char] += 1

    for letter in s2:
        if letter in occurance and occurance[letter] != 0:
            occurance[letter] -= 1
        else:
            return False
    return True


if __name__ == "__main__":
    string1 = "apple pie"
    string2 = "plea pipe"
    print(isSame(string1, string2))
    print(isPermutation(string1, string2))
