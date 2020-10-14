'''
1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of
a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A
permutation is a rearrangement of letters. The palindrome does not need to be limited to just
dictionary words.

EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat'; "atc o eta·; etc.)
'''

# O(n) time | O(n) Space
def palindromePermtation(string):
    isEven = 0
    occurances = {}
    for char in string.lower():
        if char == " ":
            continue
        isEven += 1
        if char not in occurances:
            occurances[char] = 1
        elif occurances[char] == 1:
            occurances.pop(char)
        else:
            occurances[char] -= 1
    if isEven % 2 == 0:
        return len(list(occurances.keys())) == 0

    return len(list(occurances.keys())) == 1 and occurances[list(occurances.keys())[0]] == 1


if __name__ == "__main__":
    inputString = "Tact Coa"
    print(palindromePermtation(inputString))
