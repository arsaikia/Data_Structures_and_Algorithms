# Approach 1: Reverse the String
# O(n) time || O(n) Space


def reverseStringPalindrome(string):
    revString = string[::-1]
    if string == revString:
        return True
    return False


# O(n) Time || O(1) Space
def checkPalindrome(string):
    for i in range(len(string)//2):
        if string[i] != string[len(string)-1-i]:
            return False
    return True


myString = 'MOROM'
print(f'APPROACH-1 > The String "{myString}" is a palindrome  ? ',
      reverseStringPalindrome(myString))


print(f'APPROACH-2 > The String "{myString}" is a palindrome  ? ',
      checkPalindrome(myString))
