# Naive Approach : Make another string by traversing the given one: at each step converting to lower case and checking if AlphaNum
# O( n+ n + n/2 ) = O(n) Time || O(n) Space
def naiveIsPalindrome( string ):
    revString = [i.lower() for i in string if i.isalpha()]
    revString = ''.join(revString[::-1])
    for i in range(len(revString)//2):
        if revString[i] != revString[len(revString)-i-1]:
            return False
    return True









print(naiveIsPalindrome( "race a car" ))