# O(n) Time || O(1) Space
def checkPalindrome(string):
    for i in range(len(string)//2):
        if string[i] != string[len(string)-1-i]:
            return False
    return True


myString = 'MOROM'
print(f'The String "{myString}" is a palindrome  ? ',
      checkPalindrome(myString))
