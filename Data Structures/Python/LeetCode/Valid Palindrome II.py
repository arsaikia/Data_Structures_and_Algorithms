# DOESNOT WORK << Check Next One >>
def validPalindromeXX(s):
    deletecounter = 0
    i, j = 0, len(s)-1

    while i <= j:
        print(s[i], s[j])
        if s[i] != s[j]:
            if deletecounter == 0:
                if s[i+1] == s[j]:
                    print(s[i+1], s[j])
                    deletecounter += 1
                    i += 2
                    j -= 1
                elif s[i] == s[j-1]:
                    print(s[i], s[j-1])
                    deletecounter += 1
                    i += 1
                    j -= 2
                else:
                    return False
            else:
                return False
        i += 1
        j -= 1
    return True

# ------------------< WORKS>---------------------------------------


def validPalindrome(s: str) -> bool:
    i, j = 0, len(s)-1
    while i < j:
        if s[i] != s[j]:
            if not (isPalindromeFast(s[i+1: j+1]) or isPalindromeFast(s[i: j])):
                return False
            return True
        else:
            i += 1
            j -= 1
    return True

# More time less space
def isPalindromeSlow(string) -> bool:
    strlen = len(string)
    for i in range(len(string)//2):
        if string[i] != string[strlen-i-1]:
            return False
    return True

# More Spcae less time
def isPalindromeFast(string) -> bool:
    return string == string[::-1]


print(validPalindrome(
    "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))
