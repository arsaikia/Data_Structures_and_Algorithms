"""
Given a string/array, return the character/digit without duplicate.
e.g.:   `aaabccdeefgh`  -> b, d, f, g, h each doesn't have duplicates while b is the first occurance. Return 'b'
        [1,2,3,2,3,1,4,5,5,6,6,7]   -> 4 and 7 -> op 7
"""

def findFirstNonduplicate( str):
    countDict = {}
    for i in range(len(str)):
        if str[i] not in countDict:
            countDict[str[i]] = 1
        else:
            countDict[str[i]] += 1
    for each in str:
        if countDict[each] == 1:
            return each
    return '__'

inputString = "aaabccdeefgh"
print(findFirstNonduplicate(inputString))

inputArray = [1,2,3,2,3,1,4,5,5,6,6,7]
print(findFirstNonduplicate(inputArray))