# Naive Approach : Make another string by traversing the given one: at each step converting to lower case and checking if AlphaNum
# O( n+ n + n/2 ) = O(n) Time || O(n) Space
def naiveIsPalindrome( string ):
    revString = [i.lower() for i in string if i.isalnum()]
    revString = ''.join(revString[::-1])
    for i in range(len(revString)//2):
        if revString[i] != revString[len(revString)-i-1]:
            return False
    return True

# O(n) Time || O(1) Space
def twoPointerIsPalindrome( string ):
    i, j = 0, len(string)-1
    while i<j:
        print(i, j, string[i], string[j])
        if string[i].isalnum():
            low = string[i].lower()
        else:
            i += 1
            continue

        if string[j].isalnum():
            high = string[j].lower()
        else:
            j -= 1
            continue
        if low != high:
            return False
        else:
            i+=1
            j-=1
    return True










print(twoPointerIsPalindrome( "A man, a plan, a canal: Panama" ))