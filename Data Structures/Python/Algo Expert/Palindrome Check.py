# Approach 1: String Concatination to get the reversed sring
# O(n^2) Time || O(n) Space
def stringConcatPalindrome( string ):
    revStr = ''
    for i in range(len(string)-1, -1, -1):
        revStr += string[i]
    if string == revStr:
        return True
    return False



# Approach 2: Reverse the String
# O(n) time || O(n) Space
def reverseStringPalindrome(string):
    revString = string[::-1]
    if string == revString:
        return True
    return False

# Approach 3: String into array then traverse
# O(n) time || O(n) Space
def stringarrayPalindrome( string ):
    stringArray = list(string)
    for i in range(len(stringArray)//2):
        if stringArray[i] != stringArray[len(stringArray)-i-1]:
            return False
    return True

# Approach 4: Traverse the string directly
# O(n) Time || O(1) Space
def checkPalindrome(string):
    for i in range(len(string)//2):
        if string[i] != string[len(string)-1-i]:
            return False
    return True


myString = 'MOROM'
print(f'APPROACH-2 > The String "{myString}" is a palindrome  ? ',
      reverseStringPalindrome(myString))


print(f'APPROACH-4 > The String "{myString}" is a palindrome  ? ',
      checkPalindrome(myString))
