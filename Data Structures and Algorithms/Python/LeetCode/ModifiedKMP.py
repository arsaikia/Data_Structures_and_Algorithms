
def knmuthMorrisPratt(string, substring):
    pattern = buildPattern(substring)
    count = 0
    i = 0
    while i < len(string):

        x = doesMatch(string, i, substring, pattern)
        if x != -1:
            count += 1
            i = x - (len(substring) - 1) + 1
        else:
            break
    return count


def buildPattern(substring):
    pattern = [-1 for _ in substring]
    i, j = 1, 0
    while i < len(substring):
        if substring[i] == substring[j]:
            pattern[i] = j
            i += 1
            j += 1
        elif j > 0:
            j = pattern[j - 1] + 1
        else:
            i += 1
    return pattern


def doesMatch(string, startIdx, substring, pattern):
    i, j = startIdx, 0
    while i <= len(string) - 1:
        if string[i] == substring[j]:
            if j == len(substring) - 1:
                return i
            i += 1
            j += 1
        elif j > 0:
            j = pattern[j - 1] + 1
        else:
            i += 1
    return -1


vowels = ["a", "e", "i", "o", "u", "y"]
string = "amazing"

strArray = "".join(["0" if i in vowels else "1" for i in string])
subStr = "010"
print(knmuthMorrisPratt(strArray, subStr))
