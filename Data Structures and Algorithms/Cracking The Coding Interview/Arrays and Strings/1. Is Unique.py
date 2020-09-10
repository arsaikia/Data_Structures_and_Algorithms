'''
1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures?


NOTE: Important to ask the interviewer if we have ASCII or Unicode string
    ASCII defines 128 characters, which map to the numbers 0–127. 
    Unicode defines (less than) 2^21 characters, which, similarly, 
    map to numbers 0–2^21 (though not all numbers are currently assigned, and some are reserved)
    https://stackoverflow.com/questions/19212306/whats-the-difference-between-ascii-and-unicode#:~:text=9%20Answers&text=ASCII%20defines%20128%20characters%2C%20which,%2C%20and%20some%20are%20reserved).

'''

# O(1) Time | O(1) Space
# It lloks like a O(n) operation, but because at max we will traverse 128 letters before either finding a 
# duplicate or finishing the operation, The time required will be a constant operation. Similarly for Space.
def isUniqueUsingDataStructure(string) -> bool:
    '''Considering the string we have only contains of ASCII characters. Same check can be done for Unicode'''
    if len(string) > 128:
        return False

    # Use a hashmap to store the letter occurances
    occurances = {}

    for char in string:
        if char not in occurances:
            occurances[char] = True
        else:
            return False
    return True


# O(n^2) Time | O(1) Space : No additional Data Structure
def isUnique(string):
    if len(string) > pow(2, 21):
        return False
    
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                return False
    return True
    



if __name__ == "__main__":
    string = "abcdefghijklmnopqrstuvwxyz"
    print(isUniqueUsingDataStructure(string))
    print(isUnique(string))
